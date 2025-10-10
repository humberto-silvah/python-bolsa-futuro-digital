**Exercícios de Fixação**

**1. Identifique as partes: Dada a tabela abaixo, diga:**
**Qual é a chave primária?**
**Quais são os campos?**
**Quantos registros existem?**

    R= id_produto.
    R= id_produto, nome_produto, preço, estoque.
    R= 3

**2. Relacione as tabelas: Imagine que você tem as tabelas abaixo:**
**Qual cliente fez mais pedidos?**
**Qual campo faz a ligação entre as duas tabelas?**

    R= id 1, lucas.
    R=id_cliente


**3. Raciocínio lógico:**
**Se você fosse criar um sistema para uma biblioteca, quais tabelas existiriam?**
**Quais campos cada uma delas teria?**
**Qual seria a chave primária e as chaves estrangeiras?**

    R=  Usuario(id_usuario, nome, endereço)
        Livro(id_livro, tituto, autor, ano)
        Emprestimo(id_usuario, id_livro, livro)