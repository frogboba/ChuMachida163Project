'''
File contains create_navbar method
'''
import dash_bootstrap_components as dbc


def create_navbar() -> dbc._components.NavbarSimple:
    '''
    Creates layout for navbar on Dash app
    Returns the navbar
    '''
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Alcohol", href='/alcohol'),
                    dbc.DropdownMenuItem("Caffeine", href='/caffeine'),
                    dbc.DropdownMenuItem("Exercise", href='/exercise'),
                    dbc.DropdownMenuItem("Age", href='/age'),
                    dbc.DropdownMenuItem("Smoking", href='/smoking'),
                ],
            ),
        ],
        brand="Home",
        brand_href="/",
        sticky="top",
        color="dark",
        dark=True,
    )

    return navbar
