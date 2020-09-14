require("dotenv").config()
const bodyParser = require("body-parser")
const express = require('express')
//Modulo encargado de enviar el email
const correo = require("./email")
const path = require("path")
const app  = express()

//Creacion del servidor HTTP
app.use(bodyParser.json())

app.use('/static',express.static(path.join(__dirname,"public")))

app.get("/",(req,res)=>{
    res.status(200).sendFile(path.join(__dirname,"public","index.html"))
})

app.post("/",(req,res)=>{
    correo.sendEmail(req.body,function(err,info){
        if (err) {
            res.status(400).send("Email server error")
        }
        if (info){
            res.status(200).send("Email has been sent successfully")
        }
    })
})

app.listen(process.env.PORT || 8080,()=>{
    console.log("App is running %s",process.env.PORT)
})