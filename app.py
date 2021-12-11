from flask import Flask,request,redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aimzeroemailsolution@gmail.com'
app.config['MAIL_PASSWORD'] = 'newbie123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods = ['POST'])
def index():
    client = request.form['clientname']
    service1 = request.form.get('servicelist')
    clientemail = request.form['clientemail']
    clientmessage = request.form['clientmessage']
  
  
    msg = Message(

				client+ " " + service1,
				sender ='sales@hatsoffqatar.com',
                recipients = ['sales@hatsoffqatar.com','hatsoffonline@gmail.com'],
                bcc=['basithcoder@gmail.com']
                
			)
    # msg.body = f'Client: {client} \nClient Email: {clientemail} \nService: {service} \nMessage: {clientmessage}'
    msg.html = '''<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700&display=swap" rel="stylesheet">
<script src="https://kit.fontawesome.com/c8ee3dd930.js"></script>


<body style="        font-family: 'Roboto', sans-serif;
background: #f0f5f9;">
    <div class="container">
        <div class="card" style="position: relative;
        padding: 20px;
        box-shadow: 3px 10px 20px rgba(0, 0, 0, 0.2);
        border-radius: 3px;
        border: 0;">
            <div class="title">
                <h1 style="font-size: 34px;
                font-weight: bold;
                margin-bottom: 0;">Consultation Message from {name}</h1>
            </div>
            <div class="content" style="margin-top: 25px;
           
        ">
                <table>
                    <tr>
                        <td>
                            <h3>Name </h3>
                        </td>
                        <td>
                            <h3 style="font-weight:100 ;">{name}</h3>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h3 >Email</h3>
                        </td>
                        <td>
                            <h3 style="font-weight:100 ;"><a href="mailto:{email}"></a>{email}</h3>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h3 >Services</h3>
                        </td>
                        <td>
                            <h3 style="font-weight:100 ;">{service}</h3>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h3 >Message</h3>
                        </td>

                        <td>
                            <h3 style="font-weight:100 ;">{message}</h3>
                        </td>
                    </tr>
                </table>

                <p style="text-align: center;">AimZero Emailing Solution <br> <a
                        href="http://www.aimzero.in">AimZero</a></p>

            </div>
        </div>
    </div>
</body>'''.format(name=client,email=clientemail,service=service1,message=clientmessage)
    mail.send(msg)
    return redirect('https://www.hatsoffqatar.com',code=307)

@app.route('/new')
def new():
    return "working"


if __name__=='__main__':
    app.run()