#!/usr/bin/env python3

import sys
from random import choice

def generate_friends_file(number_of_lines):

  # lista de varios nomes de pessoas
  possible_names = ['Scott', 'Miguel', 'Mervin', 'Essie', 'Lorraine', 'Earnest', 'Sharon', 'Laverne', 
  'Phyllis', 'Deanna', 'Santos', 'Joyce', 'Paula', 'Janice', 'Kelly', 'Corey', 'Gail', 'Donald', 
  'Ron', 'Kimberly', 'George', 'Lucille', 'Irma', 'Beth', 'Mary', 'Patrick', 'Elma', 'Edna', 'Irvin',
  'Ray', 'Xavier', 'Kristi', 'Glenn', 'Kenya', 'Maxine', 'Phung', 'Jacob', 'Chandra', 'Nancy', 
  'Hattie', 'Helene', 'Katrina', 'Naomi', 'Tia', 'Marvin', 'Imelda', 'Maritza', 'Kathy', 'Nathan', 
  'Jermaine', 'Hope', 'Harold', 'Tamara', 'Susan', 'Bryan', 'Irene', 'Sophie', 'Charles', 'Katelyn',
  'Brenda', 'Andrea', 'Stacey', 'Leon', 'Gayle', 'Kevin', 'Cortney', 'Haydee', 'Amy', 'Glenda', 
  'Hilda', 'Wayne', 'Andreas', 'Robert', 'Guy', 'Linda', 'Raymond', 'Florence', 'Betty', 'Cruz', 
  'Ila', 'Dee', 'Bobby', 'Crystal', 'Tisha', 'Ralph', 'Trent', 'Jenny', 'Jesse', 'Nathaniel', 
  'Brenna', 'Alexis', 'Virginia', 'Angel', 'Kenneth', 'Erin', 'Michael', 'Elva', 'Melissa', 
  'Terence', 'Thomas', 'Danielle', 'Marilyn', 'Olen', 'Rose', 'Elijah', 'Luis', 'Bernice', 
  'Reynaldo', 'Stuart', 'Dennis', 'Elizabeth', 'Julia', 'Blake', 'Elizabet', 'Sally', 'Jacques', 
  'Jesus', 'Jane', 'Ronda', 'Preston', 'Timothy', 'Patsy', 'Gordon', 'Ruth', 'Arthur', 'In', 
  'Daniel', 'Dawn', 'Doreen', 'Armando', 'Fanny', 'Anita', 'Pearlie', 'Candyce', 'Jose', 'Victor',
  'Marianne', 'Esther', 'Anna', 'Donna', 'Rosie', 'Edwin', 'Kristopher', 'Venessa', 'Sarah', 
  'Erika', 'Janell', 'Meghan', 'Ross', 'Catrina', 'Brian', 'Tim', 'Fay', 'Edward', 'Valerie', 
  'Thelma', 'Tammy', 'Lloyd', 'Myrna', 'Hong', 'Cristy', 'Joshua', 'Rhonda', 'Mildred', 'Lashon', 
  'Frances', 'Russell', 'Denise', 'Rebekah', 'Lisa', 'Kristine', 'Andre', 'John', 'Leigha', 'Joseph', 
  'Christopher', 'Manuel', 'Evan', 'Shane', 'Diane', 'Renee', 'Cheryl', 'Marisol', 'Stephen', 'Wanda', 
  'Vanessa', 'Karen', 'Laura', 'Rosia', 'William', 'Joanne', 'Clarence', 'Linsey', 'Tiffany', 'Cindy', 
  'Fabian', 'Claudia', 'Ada', 'Joao', 'Maria']

  content = ''

  # loop que constroi pares de amigos, o numero de pares eh o recebido como argumento
  for i in range(number_of_lines):

    friends_pair  = ''

    # condicao para garantir que nao colocaremos pares de amigos repetidos
    while not friends_pair or friends_pair in content:
      
      # nome de pessoa e nome do amigo aleatorios dentro da lista de nomes possiveis
      person = choice(possible_names)
      friend = choice(possible_names)

      # garantindo que uma pessoa nao eh sua propria amiga
      while person == friend:
        friend = choice(possible_names)

      # construindo par no formato "pessoa, amigo"
      friends_pair =  ("%s, %s" % (person,friend))

    # adicionando par de amigos aos pares, com uma quebra de linha no final para separar
    content += friends_pair+'\n'

  # escrevendo tudo no arquivo
  f = open("friends.txt", "w")
  f.write(content)
  f.close()


if __name__ == "__main__":
   # recebe o numero de pares de amigos desejados e chama a funcao geradora
   generate_friends_file(int(sys.argv[1]))
