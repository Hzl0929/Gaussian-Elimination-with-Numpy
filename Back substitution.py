def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.

    Parameters:
    - M (numpy.array): The augmented matrix in row echelon form with unitary pivots (n x n+1).

    Returns:
    numpy.array: The solution vector of the linear system.
    """
    
    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()

    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = M.shape[0]

    ### START CODE HERE ####
    
    # Iterate from bottom to top
    for row in reversed(range(num_rows)): 
        substitution_row = M[row]

        # Get the index of the first non-zero element in the substitution row. Remember to pass the correct value to the argument augmented.
        index = get_index_first_non_zero_value_from_row(M, row, augmented = True)

        # Iterate over the rows above the substitution_row
        for j in range(row): 

            # Get the row to be reduced. The indexing here is similar as above, with the row variable replaced by the j variable.
            row_to_reduce = M[j]

            # Get the value of the element at the found index in the row to reduce
            value = row_to_reduce[index]
            
            # Perform the back substitution step using the formula row_to_reduce -> row_to_reduce - value * substitution_row
            row_to_reduce = row_to_reduce - value * substitution_row

            # Replace the updated row in the matrix, be careful with indexing!
            M[j,:] = row_to_reduce

    ### END CODE HERE ####

     # Extract the solution from the last column
    solution = M[:,-1]
    
    return solution
