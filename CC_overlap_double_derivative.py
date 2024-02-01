def product_amplitudes_multi_dd( indices_multi):
    output = np.zeros((len(params),len(params)))
    for indices_sign in indices_multi.values():
        indices, signs = indices_sign[:, :-1], indices_sign[:, -1]
        print(signs)
        print(indices)

        signs = signs.astype(np.int8)
        signs[signs > 1] = -1
        print(signs)

        for i, ind1 in enumerate(list(set(indices.ravel()))):
            for ind2 in list(set(indices.ravel()))[i + 1:]:
                bool_indices1 = ind1 == indices

                bool_indices2 = ind2 == indices
               

                row_inds1 = np.sum(bool_indices1, axis=1, dtype=bool)
                row_inds2 = np.sum(bool_indices2, axis=1, dtype=bool)
                result_boolean = np.logical_and(row_inds1, row_inds2)

                bool_indices1[result_boolean == False] = False
                bool_indices2[result_boolean == False] = False

                bool_final = np.logical_or(bool_indices1, bool_indices2)
                
                row_inds_final= np.sum(bool_final, axis=1, dtype=bool)
                
                selected_params =params[indices]
                old_params1 = np.copy(selected_params[bool_indices1])
                old_params2 = np.copy(selected_params[bool_indices2])
                selected_params[bool_final] = 1
                output[ind1][ind2] += np.sum(np.prod(selected_params[row_inds_final], axis=1) * signs[row_inds_final])
                selected_params[bool_indices1] = old_params1
                selected_params[bool_indices2] = old_params2
                np.set_printoptions(threshold=np.inf)
                
                
            print('\n')
        return(output+output.transpose())
