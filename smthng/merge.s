default abs
section .data


section .text
    global merge

merge:

    mov eax, [edi]
    cmp eax, [esi]
    jg amore
    jl bmore


amore:
    mov eax, [edi]
    mov [edx], eax
    add edx, 4
    add edi, 4
    mov eax, [edi]
    cmp eax, 0
    mov ebx, esi
    jz finish
    jmp merge

bmore:
    mov eax, [esi]
    mov [edx], eax
    add edx, 4
    add esi, 4
    mov eax, [esi]
    cmp eax, 0
    mov ebx, edi
    jz finish
    jmp merge


finish:
    mov eax, [ebx]
    cmp eax, 0
    jz end
    mov [edx], eax
    add edx, 4
    add ebx, 4
    jmp finish

end:
