import DB
import Interact_with_DB

def main_window():
    print('Введите словом, что хотите сделать:\n \
            1. Показать \
            2. Экспорт \
            3. Импорт')
    choose = str(input(''))
    return choose

def choose_of_user(choose):
    match choose:
        case '1':
            if(DB.database_info == 'class pandas.core.frame.DataFrame'):
                print ('Пусто')
            else: print(DB.database_info)
        case '2':
            print('Выберите в каком формате вы хотите экспортировать: \
                    1. xlsx \
                    2. csv')
            choose = str(input(''))
            if(choose == 'xlsx' or choose == '1'):
                 return Interact_with_DB.export_file_xlsx(DB.database_info)
            else: 
                return Interact_with_DB.export_file_csv(DB.database_info)
        case '3':
            print('Выберите в каком формате вы хотите импортировать (словами или цифрой): \
                    1. xlsx \
                    2. csv')
            choose = str(input(''))
            if(choose == 'xlsx' or choose == '1'):
                result = Interact_with_DB.import_file_xlsx()
                return result
            else: 
                return Interact_with_DB.import_file_csv()
        case _:
            print('Что-то пошло не так. Попробуйте снова')