Tóm tắt sol: 
- Chạy file flag-checker.exe ta thấy nó yêu cầu 4 kí tự, đọc kĩ code thì nó lấy 4 kí tự này md5 rồi đem xor với đống resources. Ở hàm main còn có một hàm được chạy sau khi xor xong, vì mình thấy nó không có làm gì hết. Nên mình đoán là cái resource sau khi xor chính là hàm chính mà chúng ta cần quan tâm.
- Vì cuối file windows thường toàn null bytes, nên đem đống bytes đó đi crack thì ta được 4 kí tự là FLAG, xong đem md5 của nó đi xor với đống resource để build lại file.
- Khi build lại file, đọc đoạn đầu thì mình thấy nó dùng cái thuật gì đó, ngồi hỏi chatGPT thì biết được rằng nó là RC4, xong decrypt ra được key (nó cũng chính là iv). Xong rồi nó dùng AES CBC encrypt buffer của chúng ta rồi so sánh với một mảng nào đó.
