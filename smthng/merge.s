default abs
section .data


section .text
    global merge

merge:

    mov rax, [rdi]
    cmp rax, [rsi]
    jg amore
    jl bmore


amore:
    mov rax, [rdi]
    mov [rdx], rax
    add rdx, 4
    add rdi, 4
    mov rax, [rdi]
    cmp rax, 0
    mov rbx, rsi
    jz finish
    jmp start

bmore:
    mov rax, [rsi]
    mov [rdx], rax
    add rdx, 4
    add rsi, 4
    mov rax, [rsi]
    cmp rax, 0
    mov rbx, rdi
    jz finish
    jmp start


finish:
    mov rax, [ebx]
    cmp rax, 0
    jz end
    mov [rdx], rax
    add rdx, 4
    add rbx, 4
    jmp finish




end:

    add rsp, 1
    mov rax, 60
    mov rdi, 0
    syscall
