def calculator():
    variables = {}
    variables['__builtins__'] = {}
    
    while line := input().strip():
        
        if line.startswith("#"):
            continue  # Игнорируем комментарии

        # Обработка присваивания переменной
        if "=" in line:
            identifier, expression = map(str.strip, line.split("=", 1))
            if not identifier.isidentifier():
                print("Assignment error")
                continue
            
            try:
                # Присваиваем значение переменной
                variables[identifier] = eval(expression, variables)
            except SyntaxError:
                print("Syntax error")
            except NameError:
                print("Name error")
            except Exception:
                print("Runtime error")
        else:
            # Обработка выражения
            try:
                print(eval(line, variables))
            except SyntaxError:
                print("Syntax error")
            except NameError:
                print("Name error")
            except Exception:
                print("Runtime error")

# Запуск калькулято
calculator()