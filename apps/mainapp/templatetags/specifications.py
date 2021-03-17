from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
                <table class="table table-dark">
                    <thead>
            """        

TABLE_TAIL = """
                 </tbody>
                </table>
            """

TABLE_CONTENT = """
                    
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
      
                    </tr>
                """

PRODUCT_SPEC = {
    'notedook' : {
        'Диагональ': 'digional',
        'Тип дисплея':'display_type',
        'Частота процессора':'processor_freg',
        'Оперативная память':'ram',
        'Видеокарта':'video',
        'Время работы аккумулятора':'time_without_charge'
    },
    'smartphone': {
        'Диагональ': 'digional',
        'Тип дисплея':'display_type',
        'Разрешения экрана':'resolution',
        'Заряд аккумулятора':'accum_volume ',
        'Оперативная память':'ram',
        'Наличие слота для SD карты':'sd',
        'Максимальный объем SD карты':'sd_volume_max ',
        'Камера (Мп)':'main_cam_mp',
        'Фронтальная камера (Мп)':'frontal_cam_mp'
    }
}

#функция принимает продукт и модель найм проходится по словарю все даем все его значение
def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content

@register.filter
def product_spec(product):
    model_name = product.__class__.meta.model_name
    # привращает все в html код
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)