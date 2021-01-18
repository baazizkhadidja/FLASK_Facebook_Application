from flask import Flask, render_template, url_for, request
app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
	description = """
	Toi, tu sais comment utiliser la console! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé_e et persévérante_e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bord, tu aimes trouver des solutions à tout problèmes. N'aurais-tu pas un petit problème d'autorité? ;-  
"""
	
	return render_template('index.html',
			    user_name='Doody',
			    user_image=url_for('static',
			    filename='img/profile.png'),
			    description=description, blur=True)

from .utils import find_content


@app.route('/result/')
def result():
    gender = request.args.get('gender')
    description = find_content(gender).description
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    return render_template('result.html',
                            user_name=user_name,
                            user_image=profile_pic,
                            description=description)



#if __name__ == "__main__":
#    app.run()
