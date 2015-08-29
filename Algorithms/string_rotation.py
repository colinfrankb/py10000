def reverse(arr, start, end):
    """ reverses an array from the start to the end, where start and end
    are zero indexed """
    for i in range((end - start + 1)/2):
        arr[start+i], arr[end-i] = arr[end-i], arr[start+i]
    return arr


def rotate(arr, i):
    """ rotates an array i chars to the left """
    arr = reverse(arr, 0, i-1) # arb
    arr = reverse(arr, i, len(arr)-1) #arbr
    return reverse(arr, 0, len(arr)-1) #ba

if __name__ == "__main__":
    s = "abcdefghi"
    print("".join(rotate(list(s), 3))) # => defghiabc