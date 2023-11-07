# creo la clase is_mutant para corroborar todo el proceso del adn
def is_mutant(matrix):
    count = 0
    long = len(matrix)
    
        # creo una funcion llamada fill_matrix que sirve para rellenar la matriz, y si se ingresan caracteres invalidos, o si se ingresan mas o menos de 6 volvera a llamar a la funcion
    def fill_matrix(matrix):
        it = 0
        for i in range(long):
            it += 1
            dna_row = input(f"Ingrese la fila N{it} de la matriz separada por comas: ").split(",")
                
            if len(dna_row) != 6:
                print("cantidad de caracteres incorrecta, porfavor vuelva a ingresarlos.")
                fill_matrix(matrix)
            else:
                for j in range(long):
                    dna = dna_row[j].strip().upper()
                    if dna in ["A", "T", "C", "G"]:
                        matrix[i][j] = dna
                    else:
                        print("caracter incorrecto ")
                        return fill_matrix(matrix)         
            
    # creo la funcion rows_in_matrix que sirve para comprobar filas
# Función para revisar filas
    def rows_in_matrix(matrix):
        count2 = 0
        for i in range(6): 
            char = ''
            consecutive1 = 0

            for j in range(6):
                if matrix[i][j] == char: 
                    consecutive1 += 1
                else:
                    char = matrix[i][j] 
                    consecutive1 = 1
                if consecutive1 == 4:
                    count2 += 1
                    break

        if count2 >= 1:
            return True

        return False
           
    
    # creo la funcion columns_in_matrix que sirve para comprobar columnas
    def columns_in_matrix(matrix):
        count1 = 0
        for i in range(6):
            char = ''
            consecutive = 0

            for j in range(6):
                if matrix[j][i] == char:
                    consecutive += 1
                else:
                    char = matrix[j][i]
                    consecutive = 1
                if consecutive == 4:
                    count1 += 1
                    break
                    
        if count1 >= 1:
            return True

        return False
    
   # Función para diagonales izquierda-derecha
    # Función para diagonales izquierda-derecha
    def check_diagonals_left_right(matrix):
        count3 = 0
        for i in range(len(matrix) - 3):
            for j in range(len(matrix[0]) - 3):
                if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
                    count3 += 1

        if count3 >= 1:
            return True
        
        return False

    # Función para diagonales derecha-izquierda  
    def check_diagonals_right_left(matrix):
        count4 = 0
        for i in range(3, len(matrix)):
            for j in range(len(matrix[0]) - 3):
                if matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]:
                    count4 += 1

        if count4 >= 1:
            return True
        
        return False
            
    fill_matrix(matrix)
    print(matrix)      
    if columns_in_matrix(matrix):
        count =+1
            
    if rows_in_matrix(matrix):
        count += 1

    if check_diagonals_left_right(matrix):
        count += 1

    if check_diagonals_right_left(matrix):
        count += 1

    if count >= 2:
        
        return True
    else:
        
        return False
   
 
# creo el main
print("Hola, soy Magneto, necesito que ingreses tu adn para saber si eres mutante o no. ")
dna_matrix = [[""]*6 for i in range(6)]
if is_mutant(dna_matrix):
    print("Eres mutante")
else:
    print("No eres mutante")