 // Не забудьте поместить этот класс в нужный пакет
 package spbu.iggs.hw2.task3;

 import java.util.ArrayList;

 public class Library {
    private String address;
    private static final String opening_hours = "Каждый день с 9 до 17";
    private ArrayList<Book> books = new ArrayList<>();
    // Сюда надо добавить недостающие методы

     private void borrowBook(String title) {
        int pos = -1;
        for (int i = 0; i < books.size(); i ++) {
            if (books.get(i).getTitle().equals(title)){
                pos = i;
            }
        }

        if (pos != -1) {
            if (books.get(pos).isBorrowed()) {
                System.out.println("Извините, книга уже взята");
            }
            else {
                this.books.get(pos).borrowed();
                System.out.println("Вы успешно взяли книгу " + (books.get(pos).getTitle()));
            }
        }
        else{
            System.out.println("Такой книги нет...");
        }
    }


      private void returnBook(String title){
        int pos = -1;
        for (int i = 0; i < books.size(); i ++) {
             if (books.get(i).getTitle().equals(title)){
                 pos = i;
             }
         }

         if (pos != -1) {
             if (this.books.get(pos).isBorrowed()) {
                 this.books.get(pos).returned();
                 System.out.println("Вы успешно вернули книгу");
             }
             else {
                 System.out.println("Эту книгу никто не брал");
             }
         }
         else{
             System.out.println("Такой книги нет...");
         }
     }


     private static void printOpeningHours(){
        System.out.println(opening_hours);
    }

    private void printAddress(){
        System.out.println(address);
    }

    public Library(String address){
        this.address = address;

    }
    private void addBook(Book book){
        this.books.add(book);
        System.out.println("Книга " + (books.get(books.size() - 1).getTitle()) + " успешно добавлена");
    }

    private void printAvailableBooks(){
        boolean flag = true;
        if (this.books.size() != 0) {
            for (int i = 0; i < books.size(); i++) {
                if (!books.get(i).isBorrowed()) {
                    System.out.println(books.get(i).getTitle()); // Если в библиотеке есть доступные книги
                    flag = false;
                }
            }
            if(flag){
                System.out.println("Все книги арендованы"); // Если в библиотеке есть книги, но они недоступны
            }
        }
        else{
            System.out.println("В библиотеке нет книг"); // Если в библиотеке вообще нет книг
        }
    }

    public static void main(String[] args) {
        // Создаем две библиотеки
        Library firstLibrary = new Library("Университетский пр., 120");
        Library secondLibrary = new Library("Московский пр., 86");

        // Добавляем четыре книги в первую библиотеку
        firstLibrary.addBook(new Book("Код да Винчи")); // При добавлении на экран должно выводиться сообщение об успешном добавлении соответствующей книги
        firstLibrary.addBook(new Book("50 оттенков серого"));
        firstLibrary.addBook(new Book("Учебник мемологии"));
        firstLibrary.addBook(new Book("Властелин Колец"));

        // Выводим на экран часы работы и адреса
        System.out.println("Часы работы библиотек:");
        printOpeningHours(); // Что-то типа "Все библиотеки работают с понедельника по субботу с 9 до 18", текст на ваше усмотрение
        System.out.println();

        System.out.println("Адреса библиотек:");
        firstLibrary.printAddress(); // Выводит адрес
        secondLibrary.printAddress();
        System.out.println();

        // Пытаемся взять Властелина Колец из обеих библиотек
        System.out.println("Берем лучшую книгу на земле:");
        firstLibrary.borrowBook("Властелин Колец");   // Должно пройти успешно, мы должны получить соответствующее сообщение об успехе
        firstLibrary.borrowBook("Властелин Колец");   // Книга уже взята, об этом нам должны написать
        secondLibrary.borrowBook("Властелин Колец");  // Такой книги нет в каталоге, это тоже отдельное сообщение для нас
        System.out.println();
        // Выводим названия всех книг в обеих библиотеках


        System.out.println("Доступные книги в первой библиотеке:");
        firstLibrary.printAvailableBooks();  // Только список книг, которые можно взять
        System.out.println();
        System.out.println("Доступные книги во второй библиотеке:");
        secondLibrary.printAvailableBooks(); // Так как во вторую книг не добавляли, то тут надо написать что-то типа "В каталоге пусто"
        System.out.println();

        // Возвращаем Властелина Колец в первую библиотеку
        System.out.println("Прочитали Властелина Колец, возвращаем:");
        firstLibrary.returnBook("Властелин Колец"); // Сообщение об успешном возвращении
        System.out.println();

        // Снова выводим список доступных книг в первой библиотеке
        System.out.println("Доступные книги в первой библиотеке:");
        firstLibrary.printAvailableBooks();
    }
}