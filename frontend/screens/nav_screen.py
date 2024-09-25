import flet as ft

# Função de navegação
def show_nav(page: ft.Page):
    def on_navigation_change(e):
        # Atualiza a página com base na aba selecionada
        if e.control.selected_index == 0:
            show_home_page()
        elif e.control.selected_index == 1:
            show_table_page()
        elif e.control.selected_index == 2:
            show_about_page()
        elif e.control.selected_index == 3:
            logout()

    # Funções para cada tela
    def show_home_page():
        page.controls.clear()
        page.add(
            ft.Container(
                content=ft.Text("Bem-vindo ao sistema de governaça de dados da CPFL!", style="headlineMedium"),
                alignment=ft.alignment.center,
                expand=True,
            )
        )
        page.update()

    def show_table_page():
        page.controls.clear()
        page.add(
            ft.Container(
                content=ft.Text("Aqui está a lista de tabelas!", style="headlineMedium"),
                alignment=ft.alignment.center,
                expand=True,
            )
        )
        page.update()

    def show_about_page():
        page.controls.clear()
        page.add(
            ft.Container(
                content=ft.Text("O sistema de governaça de dados tem por objetivo fazer a gestão aqui você pode requerer seus acessos a dados.", style="headlineMedium"),
                alignment=ft.alignment.center,
                expand=True,
            )
        )
        page.update()

    # Função de logout
    def logout():
        page.controls.clear()
        page.add(show_login_form())
        page.update()

    # Menu de navegação lateral com espaçamento
    navigation_rail = ft.NavigationRail(
        selected_index=0,  # Index inicial
        on_change=on_navigation_change,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.icons.TABLE_CHART, label="Ver Tabelas"),
            ft.NavigationRailDestination(icon=ft.icons.INFO, label="Sobre"),
            ft.NavigationRailDestination(icon=ft.icons.EXIT_TO_APP, label="Logout"),
        ],
        expand=True,
        label_type=ft.NavigationRailLabelType.ALL
    )

    # Inicializa a tela com a Home
    show_home_page()

    # Adiciona a Navigation Rail na lateral da página
    page.add(
        ft.Row(
            [
                navigation_rail,  # Usamos o NavigationRail diretamente
                ft.VerticalDivider(width=1),
                ft.Container(expand=True),  # Container expansível para o conteúdo principal
            ],
            expand=True  # Expande o Row para preencher a tela
        )
    )
    page.update()