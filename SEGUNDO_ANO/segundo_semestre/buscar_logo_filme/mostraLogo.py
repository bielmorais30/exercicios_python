import easygui as easygui
from app import buscarFilme
import PIL
nome = input("filme: ")
buscarFilme(nome)

easygui.msgbox(nome, image="Poster_Filme.jpg")
