 // Не забудьте поместить этот класс в нужный пакет
 package spbu.iggs.hw2.task3;

 public class Library {
    private static final  int size = 10;
    private String address;
    private int pointer = 0; // Костыль для добавления книги в библиотеку, по сути это номер заполняемой ячейки массива
    private static final String openinghours = "Каждый день с 9 до 17";
    Book[] books = new Book[size];
    // Сюда надо добавить недостающие методы

    public void borrowBook(String title) {
        int pos = -1;
        for (int i = 0; i < pointer; i ++) {
            if (books[i].getTitle().equals(title)){
                pos = i;
            }
        }

        if (pos != -1) {
            if (this.books[pos].isBorrowed()) {
                System.out.println("Извините, книга уже взята");
            }
            else {
                this.books[pos].borrowed();
                System.out.println("Вы успешно взяли книгу " + (books[pos].getTitle()));
            }
        }
        else{
            System.out.println("Такой книги нет...");
        }
    }


     public void returnBook(String title){
        int pos = -1;
        for (int i = 0; i < pointer; i ++) {
             if (books[i].getTitle().equals(title)){
                 pos = i;
             }
         }

         if (pos != -1) {
             if (this.books[pos].isBorrowed()) {
                 this.books[pos].returned();
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


     public static void printOpeningHours(){
        System.out.println(openinghours);
    }

    public void printAddress(){
        System.out.println(address);
    }

    Library(String address){
        this.address = address;

    }
    public void addBook(Book book){
        if (pointer <= size - 1){
        this.books[pointer] = book;
        System.out.println("Книга " + (books[pointer].getTitle()) + " успешно добавлена");
        pointer += 1; // Когда я делал это задание у меня был очень плохой инет и я не мог узнать, как нормально добавлять элемент в массив

        }
        else{
            System.out.println("В библиотеке нет места!");
        }
    }

    public void printAvailableBooks(){
        for (int i = 0; i < pointer; i ++){
            if (books[i].isBorrowed()){}
            else{
                System.out.println(books[i].getTitle());
            }
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