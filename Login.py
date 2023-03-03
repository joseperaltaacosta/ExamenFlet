import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6

    dlg = ft.AlertDialog(title=ft.Text("CONTRASEÑA CORRECTA!"))

    def login(e):
        if tfnombre.value==tfpassword.value:
            page.dialog = dlg
            dlg.open = True
            page.update()

    #Fin --- Ejercicio 6


    #Ejercicio 2
    

    img = ft.Image(src=f"Logo.png",width=100,height=100,fit=ft.ImageFit.CONTAIN,)
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.window_height=500
    page.window_width= 250
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.update()

    #Fin --- Ejercicio 3

    tfnombre = ft.TextField(label="Nombre")
    
    #Ejercicio 5

    btnEntrar=ft.ElevatedButton("GUARDAR",icon="settings",on_click=login)

    #Fin-- Ejercicio 5


    #Ejercicio 4
    
    tfpassword=ft.TextField(label="Contraseña", password=True, can_reveal_password=True)

    #Fin --- Ejercicio 4

    page.add(img,tfnombre,tfpassword,btnEntrar)


ft.app(target=main,assets_dir="fotos")