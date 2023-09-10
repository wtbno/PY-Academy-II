"""
* Escopo de funções
Escopo => O que é definido dentro da função, fica 'protegido' naquela função
** Existe o escopo local e o escopo global
=> Local é onde apenas nomes do mesmo podem ser alcançados
Variáveis definidas dentro de uma função são consideradas variáveis de escopo local.
Essas variáveis só podem ser acessadas dentro da função onde foram definidas.
O escopo local é criado sempre que uma função é chamada e destruído quando a função termina de ser executada.

=> Global é o escopo alcançavel por todo o código
Variáveis definidas fora de todas as funções são consideradas variáveis de escopo global.
Essas variáveis podem ser acessadas e modificadas em qualquer lugar do código, dentro ou fora das funções.
Variáveis globais são declaradas fora de qualquer função e geralmente são usadas para armazenar dados que precisam ser compartilhados entre várias partes do programa.

É importante ter cuidado ao trabalhar com variáveis globais, pois elas podem ser modificadas em diferentes partes do programa, tornando o código mais difícil de entender e depurar. Em geral, é uma prática recomendada usar variáveis locais sempre que possível e passar valores para funções como argumentos em vez de depender de variáveis globais.

"""


# => Exemplo escopo local:
def escopo():
    x = 1  # x é uma variável de escopo local
    print(x)


escopo()  # Chamando a função
# print(x)  # Isso resultará em um erro, pois x não está definido no escopo global


y = 10  # x é uma variável de escopo global


def minha_funcao():
    global y  # Manipulando uma var global dentro do escopo
    y = 13
    print(y)  # É possível acessar a variável global x dentro da função


minha_funcao()  # Chamando a função
# A variável x pode ser acessada fora da função também
print(f'{y}, "y" com valor de 10 devido ser var global ')


def escopo_demo():

    y = 58  # essa não é a mesma var acima devido estar dentro de outro escopo

    def outra_funcao():
        z = 3
        print(f'{y} {z}, mostrando "y" do escopo_demo e o "z"  de outra_funcao ')

    outra_funcao()
    print(f'{y} , mostrando "y" ainda dentro do escopo_demo')


escopo_demo()
print(f'{y}, "y" com valor de 10 devido ser var global fora do escopo_demo ')

"""
Primeiro, você define uma variável global chamada y e atribui a ela o valor 10.

Em seguida, você define uma função chamada escopo. Dentro dessa função, você define outra função chamada outra_funcao.

Dentro da função outra_funcao, você define uma variável local chamada z e atribui a ela o valor 3.

Em seguida, você imprime o valor das variáveis y e z. A função outra_funcao imprime esses valores, mas como y não foi definido dentro da função outra_funcao, ela procura por uma variável chamada y no escopo mais amplo, que é a função escopo. Como y foi definido como uma variável global, ele é acessível em qualquer lugar do código, e o valor 10 será impresso para y e 3 para z.

Após chamar outra_funcao, você chama print(y) novamente dentro da função escopo. Neste caso, a função escopo tem acesso direto à variável global y, então ela imprimirá novamente o valor 10 para y.

Portanto, quando você chama a função escopo, ela imprime "10 3" para y e z respectivamente, e depois imprime "10" novamente para y. Isso acontece porque as variáveis locais definidas em uma função têm precedência sobre as variáveis globais com o mesmo nome quando você tenta acessá-las dentro dessa função.

"""


"""
Precedência

Em Python, a precedência de funções refere-se à ordem em que o interpretador Python busca por uma função com um determinado nome quando você a chama. O Python segue uma hierarquia específica para determinar qual função deve ser executada, e essa hierarquia é chamada de "escopo". Aqui estão os níveis de precedência de funções em Python, do mais específico para o mais amplo:

Local (Escopo mais interno): O Python começa procurando a função no escopo local, ou seja, dentro da função atual onde a chamada está sendo feita. Se a função estiver definida nesse escopo, ela será chamada. Caso contrário, o Python continuará a busca.

Enclosing (Escopo envolvente): Se a função não for encontrada no escopo local, o Python procurará no escopo envolvente. Esse escopo envolvente ocorre quando você tem funções aninhadas (uma função definida dentro de outra). O Python irá subir para o escopo que envolve a função atual para procurar a função chamada.

Global (Escopo global): Se a função não for encontrada no escopo local nem no escopo envolvente, o Python procurará no escopo global. O escopo global é o nível mais amplo e contém variáveis e funções que estão definidas no nível superior do seu programa.

Built-in (Funções internas): Se a função não for encontrada nos escopos anteriores, o Python verificará as funções incorporadas (built-in) do Python. Estas são funções que estão disponíveis em qualquer lugar do seu código Python sem a necessidade de importações específicas, como print(), len(), range(), etc.

Se o Python não encontrar a função em nenhum desses escopos, ele gerará uma exceção chamada NameError, indicando que a função não foi definida.

É importante entender a precedência de funções em Python, pois isso afeta como o Python resolve quais funções serão chamadas quando você utiliza o mesmo nome de função em diferentes escopos do seu código. Normalmente, o Python seguirá a ordem de escopo mencionada acima para determinar qual função deve ser executada.


"""
