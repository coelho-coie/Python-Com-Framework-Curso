import PySimpleGUI as sg
import time
import webbrowser
import random

# --- LINKS DA DOPAMINA (Vídeos aleatórios satisfatórios / hipnóticos) ---
VIDEOS_DOPAMINA = [
    "https://www.youtube.com/watch?v=n_Dv4JMiwK8",  # Parku mine
    "https://youtu.be/L_fcrOyoWZ8?si=LrosI1Rz85UASjVi",  # Gameplay de Subway Surfers 
]

# --- PALETA CYBER-DOPAMINA ---
COLOR_BG = '#05050A'          
COLOR_PANEL_IDLE = '#0F0F1A'  
COLOR_PANEL_RUN = '#1A0022'   
COLOR_NEON_CYAN = '#00F5FF'   
COLOR_NEON_PINK = '#FF007F'   
COLOR_GREEN_GLOW = '#39FF14'  
COLOR_TEXT_MUTED = '#4B4B75'  

FONT_CLOCK = 'Consolas'
FONT_UI = 'Impact'            

sg.set_options(
    background_color=COLOR_BG,
    text_element_background_color=COLOR_BG,
    element_background_color=COLOR_BG,
    button_element_size=(14, 2)
)

# --- LAYOUT ---
layout = [
    [sg.VPush()],
    
    [sg.Push(), sg.Text('⚡ MAXIMUM HYPER-STIMULUS CHRONO ⚡', font=(FONT_UI, 11), text_color=COLOR_TEXT_MUTED), sg.Push()],
    [sg.Sizer(1, 5)],
    
    [sg.Push(),
     sg.Column([
         [sg.Sizer(40, 15)],
         [sg.Push(), sg.Text('00:00.00', font=(FONT_CLOCK, 58, 'bold'), text_color=COLOR_NEON_CYAN, background_color=COLOR_PANEL_IDLE, key='-TEMPO-'), sg.Push()],
         [sg.Push(), sg.Text('STATUS: WAITING INPUT', font=(FONT_UI, 10), text_color=COLOR_TEXT_MUTED, background_color=COLOR_PANEL_IDLE, key='-STATUS-'), sg.Push()],
         [sg.Sizer(40, 15)]
     ], background_color=COLOR_PANEL_IDLE, key='-CARD-', element_justification='center'),
     sg.Push()],
    
    [sg.Sizer(1, 20)],
    
    [
        sg.Push(), 
        sg.Button('GO! / RUN', key='-START-', border_width=0, font=(FONT_UI, 14),
                  button_color=('#000000', COLOR_GREEN_GLOW), mouseover_colors=('#000000', '#2DE00F')), 
        
        sg.Sizer(12, 1), 
        
        sg.Button('PAUSE', key='-PAUSE-', border_width=0, font=(FONT_UI, 14),
                  button_color=('#FFFFFF', COLOR_NEON_PINK), mouseover_colors=('#FFFFFF', '#D10068')), 
        
        sg.Sizer(12, 1),
        
        sg.Button('RESET', key='-RESET-', border_width=0, font=(FONT_UI, 14),
                  button_color=('#FFFFFF', '#252538'), mouseover_colors=('#FFFFFF', '#3A3A54')), 
        sg.Push()
    ],
    
    [sg.VPush()]
]

window = sg.Window('HYPER CLOCK // OVERDRIVE', layout, size=(520, 360), resizable=True, finalize=True, background_color=COLOR_BG)
window.set_min_size((460, 320))

tempo_inicio = 0
tempo_decorrido = 0
pausado = True

while True:
    event, values = window.read(timeout=16) 
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-START-':
        if pausado:
            tempo_inicio = time.time() - tempo_decorrido
            pausado = False
            
            # 🔥 INJEÇÃO DE DOPAMINA VIRTUAL: Abre o vídeo aleatório no navegador!
            video_aleatorio = random.choice(VIDEOS_DOPAMINA)
            webbrowser.open(video_aleatorio)
            
            # Correção hacker do Tkinter para mudar a cor de fundo
            window['-CARD-'].Widget.configure(background=COLOR_PANEL_RUN)
            window['-TEMPO-'].update(background_color=COLOR_PANEL_RUN, text_color=COLOR_GREEN_GLOW)
            window['-STATUS-'].update('STATUS: REWARD UNLOCKED // RUNNING', background_color=COLOR_PANEL_RUN, text_color=COLOR_GREEN_GLOW)
            window.refresh()
    
    if event == '-PAUSE-':
        if not pausado:
            pausado = True
            tempo_decorrido = time.time() - tempo_inicio
            
            window['-CARD-'].Widget.configure(background=COLOR_PANEL_IDLE)
            window['-TEMPO-'].update(background_color=COLOR_PANEL_IDLE, text_color=COLOR_NEON_PINK)
            window['-STATUS-'].update('STATUS: FOCUS LOST // PAUSED', background_color=COLOR_PANEL_IDLE, text_color=COLOR_NEON_PINK)
            window.refresh()

    if event == '-RESET-':
        tempo_inicio = 0
        tempo_decorrido = 0
        pausado = True
        
        window['-CARD-'].Widget.configure(background=COLOR_PANEL_IDLE)
        window['-TEMPO-'].update('00:00.00', background_color=COLOR_PANEL_IDLE, text_color=COLOR_NEON_CYAN)
        window['-STATUS-'].update('STATUS: WAITING INPUT', background_color=COLOR_PANEL_IDLE, text_color=COLOR_TEXT_MUTED)
        window.refresh()

    if not pausado:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicio
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido % 60)
        centesimos = int((tempo_decorrido % 1) * 100)
        window['-TEMPO-'].update(f'{minutos:02d}:{segundos:02d}.{centesimos:02d}')

window.close()