import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

#
# content = html.Nav(className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top",
#                    children=[html.A(className="navbar-brand", href="https://www.pennmedicine.org",
#                                     children=[html.Img(className="container",
#                                                        src="https://www.pennmedicine.org/Assets/PennMedicine/built/images/assets/logo-white.svg")]
#                                     ),
#                              html.Button(className='navbar-toggler', children=[
#                                  html.Span(className='navbar-toggler-icon')
#                              ]),
#                              html.Div(className='collapse navbar-collapse', id='navbarSupportedContent',
#                                       children=[
#                                           html.Ul(className='navbar-nav mr-auto',
#                                                   children=[
#                                                       html.Li(className='nav-item active',
#                                                               children=[
#                                                                   html.A('CHIME 2', className='nav-link',
#                                                                          href='/')
#                                                               ]),
#                                                       html.Li(className='nav-item active',
#                                                               children=[
#                                                                   html.A('Dashboard', className='nav-link',
#                                                                          href='/dashboard/')
#                                                               ]),
#                                                       html.Li(className='nav-item active',
#                                                               children=[
#                                                                   html.A('Contributors', className='nav-link',
#                                                                          href='/contributors/')
#                                                               ]),
#                                                       html.Li(className='nav-item active',
#                                                               children=[
#                                                                   html.A('Guide', className='nav-link',
#                                                                          href='/')
#                                                               ]),
#                                                       html.Li(className='nav-item active',
#                                                               children=[
#                                                                   html.A('About', className='nav-link',
#                                                                          href='/about/')
#                                                               ]),
#                                                   ])
#                                       ])
#                              ])
