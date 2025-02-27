# Definimos los personajes 
define conductor = Character("Conductor")
define Maira = Character("Maira")
define Lucía = Character("Lucía")
define Carlos = Character("Carlos")

# Variables para la decisión final
default mataste_cinco = True  # Por defecto, mueren cinco personas

# Definimos la pantalla de inicio
label splashscreen:
    scene bg_inicio with fade

    pause 2.0

    show text "{color=#f00}{size=+20}El Dilema del Tranvía" at truecenter with dissolve
    pause 3.0

    jump start

# Comienza la historia
label start:
    scene bg_image with dissolve
    show chofer_manejando at center with dissolve

    conductor "Eres el conductor de un tranvía que ha perdido los frenos."
    conductor "En la vía principal, hay cinco personas atadas a los rieles. En la vía secundaria, solo una persona."
    conductor "Pero antes de decidir, los pasajeros comienzan a debatir qué hacer."

    # Primera decisión
    show joven_idealista_pensando at right with dissolve
    "Maira" "Una persona puede tener más dinero que las otras cinco,.. ¿Debo elegir matar a las cinco?"
    
    menu:
        "Sí, porque el dinero tiene más valor en la sociedad.":
            $ respuesta_uno = renpy.input("¿Por qué decidiste eso?")
            jump decision_dos

        "No, porque todas las vidas tienen el mismo valor.":
            $ respuesta_uno = renpy.input("¿Por qué decidiste eso?")
            jump decision_dos

label decision_dos:
    scene bg_debate with dissolve
    show mujer_seria_pensando at left with dissolve

    "Lucía" "Pero cinco personas tienen derechos, ¿no deberíamos salvar la mayoría?"
    
    menu:
        "Sí, porque más personas con derechos deben ser salvadas.":
            $ respuesta_dos = renpy.input("¿Por qué decidiste eso?")
            jump decision_tres

        "No, porque no debemos decidir sobre la vida de alguien.":
            $ respuesta_dos = renpy.input("¿Por qué decidiste eso?")
            jump decision_tres

label decision_tres:
    scene bg_debate with dissolve
    show pasajero_nervioso_serio at right with dissolve

    "Carlos" "¿Y si una de esas personas fuera un médico que podría salvar muchas vidas?"
    
    menu:
        "Salvar al médico porque su vida es más valiosa para la sociedad.":
            $ respuesta_tres = renpy.input("¿Por qué decidiste eso?")
            jump decision_cuatro

        "No, porque todas las vidas son igualmente valiosas.":
            $ respuesta_tres = renpy.input("¿Por qué decidiste eso?")
            jump decision_cuatro

label decision_cuatro:
    scene bg_debate with dissolve
    show mujer_seria_reflexionando at center with dissolve

    "Lucía" "Pero ¿y si esas cinco personas fueran criminales y la otra persona solo un empleado?"
    
    menu:
        "Mover la palanca y salvar a la persona inocente.":
            $ respuesta_cuatro = renpy.input("¿Por qué decidiste eso?")
            $ mataste_cinco = False  # Se acciona la palanca y muere una persona
            jump decision_cinco

        "No hacer nada y dejar que mueran los cinco criminales.":
            $ respuesta_cuatro = renpy.input("¿Por qué decidiste eso?")
            jump decision_cinco

label decision_cinco:
    scene bg_debate with dissolve
    show joven_idealista_reflexionando at right with dissolve

    "Maira" "Pero esas cinco personas son ancianas y la otra es una mujer joven, ¿qué hacemos?"
    
    menu:
        "Salvar a la mujer joven porque tiene más vida por delante.":
            $ respuesta_cinco = renpy.input("¿Por qué decidiste eso?")
            jump decision_final

        "Salvar a los ancianos porque su vida también vale.":
            $ respuesta_cinco = renpy.input("¿Por qué decidiste eso?")
            jump decision_final

label decision_final:
    scene bg_imagen_conclusion with fade
    show chofer_reflexionando at center with dissolve

    if mataste_cinco:
        conductor "Tomaste la decisión de NO accionar la palanca. El tranvía siguió su curso y atropelló a cinco personas."
    else:
        conductor "Tomaste la decisión de accionar la palanca. El tranvía cambió de vía y atropelló a una persona."

    conductor "Aquí están todas las razones que diste a lo largo de la historia:"

    # Mostrar las justificaciones en pantalla
    window hide
    scene bg_imagen_conclusion with fade
    show text "{color=#f00}{size=+20}Tus Justificaciones:" at truecenter with dissolve
    pause 2.0

    show text "{size=+10}" + respuesta_uno + "\n" + respuesta_dos + "\n" + respuesta_tres + "\n" + respuesta_cuatro + "\n" + respuesta_cinco at Position(xpos=0.2, ypos=0.4)
    pause 6.0

    conductor "Finalmente, reflexiona sobre tu decisión."

    $ respuesta_final = renpy.input("Escribe tu reflexión final sobre la decisión que tomaste.")

    scene bg_inicio with fade
    show text "{color=#f00}{size=+20}Fin del dilema" at truecenter with dissolve
    pause 3.0

    return
