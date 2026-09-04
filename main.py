from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import subprocess
import json

class ReproductorApp(App):
    def build(self):
        self.label = Label(text="Esperando música...", font_size=20, color=(1, 1, 1, 1))
        Clock.schedule_interval(self.actualizar_notificacion, 5)
        return self.label

    def actualizar_notificacion(self, dt):
        try:
            resultado = subprocess.run(['termux-notification-list'], capture_output=True, text=True)
            if resultado.returncode == 0 and resultado.stdout.strip():
                notificaciones = json.loads(resultado.stdout)
                for notif in notificaciones:
                    if "youtube" in notif.get("packageName", "").lower():
                        titulo = notif.get("title", "Reproduciendo")
                        self.label.text = f"Reproduciendo:\n{titulo}"
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    ReproductorApp().run()
