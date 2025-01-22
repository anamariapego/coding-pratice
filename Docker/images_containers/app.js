const express = require('express')
const app = express() // inicialização
const port = 3000

// rota get
app.get('/', (req, res) => {
    res.send('Uau! Sua imagem foi criada com sucesso!!! :)')

})

// log que vai aparecer no terminal informando a porta que aplicação está rodando
app.listen(port, () => {
    console.log( `Executando na porta: ${port}`)
});