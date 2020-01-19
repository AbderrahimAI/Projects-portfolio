
quicksortExplain = "T"

quicksortPseudo = "Quicksort Pseudocode:\n\n" \
                  "quickSort(arr[], low, high){\n" \
                  "     if (low > high){\n" \
                  "         /* pi is partitioning index, arr[pi] is now at right place */\n" \
                  "         pi = partition(arr, low, high);\n" \
                  "         quickSort(arr, low, pi - 1); // Before pi\n" \
                  "         quickSort(arr, pi + 1, high); // After pi\n" \
                  "     }\n" \
                  "}"

insertsortExplain = "Tri insertion"
insertsortPseudo = "aa"

bubblesortExplain = "Tri"

bubblesortPseudo = "Bubblesort Pseudocode:\n\n" \
                   "bubbleSort(arr){\n" \
                   "    for (n=length(arr); n>1; --n){\n" \
                   "        for (i=0; i<n-1; ++i){\n" \
                   "            if (A[i] > A[i+1]){\n" \
                   "                arr.swap(i, i+1)\n" \
                   "            } \n" \
                   "        }\n" \
                   "    }\n" \
                   "}"


