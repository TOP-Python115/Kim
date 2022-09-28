def counter(func):
    def wrapper(*args, **kwargs):
        file_path ="D:\python projects\hw\HW_06.14\log.txt"
        with open(file_path, 'a') as f_in:
            f_in.write(func.__name__ + '\n')
        return func(*args, **kwargs)
    return wrapper
    
#добавил функцию в каждый модуль, кроме main
#обернул каждую функцию в декоратор
#пришлось создать переменную-путь к файлу 'data.ini' в модуле players.py

# show_message	    2
# read_ini	        1
# show_help	        1
# show_field	    6
# player_name	    2
# game_mode	        1
# check_saves	    1
# game	            1
# check_win_or_tie	5
# check_win	        5
# random_turn	    2
# modify_stats	    1
# show_stats	    1
