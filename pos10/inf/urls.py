from django.urls import path, include

#from .views import BarrioView, BarrioNew, BarrioEdit, barrioInactivar

from .views import prediccionSeleccion
from .reportes import imprimir_prediccion

urlpatterns = [
    path('informes/',prediccionSeleccion, name="prediccion_seleccion"),
    #path('barrios/new',BarrioNew.as_view(), name="barrio_new"),
    #path('barrios/<int:pk>',BarrioEdit.as_view(), name="barrio_edit"),
    #path('barrios/estado/<int:id>',barrioInactivar, name="barrio_inactivar"),
    
    path('informes/prediccion-seleccion',imprimir_prediccion, name="informe_prediccion_todos"),
    path('informes/prediccion-todas/<str:f1>/<str:f2>/<str:segmento>',imprimir_prediccion, name="informe_prediccion_todos"),
]