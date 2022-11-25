KV = """
MDFloatLayout:
    MDBottomNavigation:
        text_color_active: "lightgrey"
    
        MDBottomNavigationItem:
            name: "Bots"
            text: "Bots"
            icon: "android"
                
            AnchorLayout:
                id: bot
    
        MDBottomNavigationItem:
            name: "Add-Bots"
            text: "Add-Bots"
            icon: "database-edit"
    
            MDIconButton:
                pos_hint: {"center_x":.5,"center_y":.75}
                icon: "plus"
                on_press: app.press("add",root.ids.prefix.text)
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                    
            MDTextField:
                hint_text: "Enter Prefix"
                pos_hint: {"center_x":.18,"center_y":.95}
                id: prefix
                size_hint_x: .15
                    
            MDTextField:
                hint_text: "Enter Name"
                pos_hint: {"center_x":.45,"center_y":.95}
                id: name
                size_hint_x: .25
                    
            MDTextField:
                hint_text: "Enter ID"
                pos_hint: {"center_x":.75,"center_y":.95}
                id: id
                size_hint_x: .3

            MDTextField:
                hint_text: "Enter Token"
                pos_hint: {"center_x":.5,"center_y":.85}
                id: token
                size_hint_x: .8

            MDRectangleFlatButton:
                id: remove_all
                pos_hint: {"center_x":.55,"center_y":.4}
                text: "Remove All Row"
                on_press: app.press("delete-all")
                
            MDTextField:
                hint_text: "Enter ID for delete"
                id: id_delete
                pos_hint: {"center_x":.25,"center_y":.25}
                size_hint_x: .3
            MDRectangleFlatButton:
                id: remove_id
                pos_hint: {"center_x":.55,"center_y":.25}
                text: "Remove with ID"
                on_press: app.press("delete_id")
                
            MDTextField:
                hint_text: "Enter ID"
                pos_hint: {"center_x":.25,"center_y":.1}
                id: id_change
                size_hint_x: .3
            MDTextField:
                hint_text: "Enter New Prefix"
                pos_hint: {"center_x":.55,"center_y":.1}
                id: prefix_change
                size_hint_x: .15
            MDRectangleFlatButton:
                id: new_prefixe
                pos_hint: {"center_x":.8,"center_y":.1}
                text: "Add New Prefix"
                on_press: app.press("change_prefix")
        MDBottomNavigationItem:
            name: "Change-Lang"
            text: "Change-Lang"
            icon: "earth"

            MDRectangleFlatButton:
                id: fr
                pos_hint: {"center_x":.5,"center_y":.75}
                text: "Français"
                on_press: app.change_language("francais")
            MDRectangleFlatButton:
                id: an
                pos_hint: {"center_x":.5,"center_y":.5}
                text: "Anglais"
                on_press: app.change_language("anglais")
            MDRectangleFlatButton:
                id: po
                pos_hint: {"center_x":.5,"center_y":.25}
                text: "Portugais"
                on_press: app.change_language("portugais")
"""