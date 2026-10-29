default abs
section .data


section .text
    global merge

merge:
    mov r10, rdx

merged:

    mov eax, [rdi]
    cmp eax, [rsi]
    jg amore
    jl bmore


amore:
    mov eax, [rdi]
    mov [r10], eax
    add r10, 4
    add rdi, 4
    mov eax, [rdi]
    cmp eax, 0
    mov rbx, rsi
    jz finish
    jmp merge

bmore:
    mov eax, [rsi]
    mov [r10], eax
    add r10, 4
    add rsi, 4
    mov eax, [rsi]
    cmp eax, 0
    mov rbx, rdi
    jz finish
    jmp merge


finish:
    mov eax, [rbx]
    cmp eax, 0
    jz end
    mov [r10], eax
    add r10, 4
    add rbx, 4
    jmp finish
end:
    ret
