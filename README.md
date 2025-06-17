<a id="readme-top"></a>

<div align="center">
  <h1 align="center">Latin Numeral Translator and Quiz</h1>


  <img src="https://github.com/BlackBaron94/Latin-Numerals-Translator-and-Quiz/actions/workflows/tests.yml/badge.svg" alt="Tests"/>
  <a href="https://codecov.io/gh/BlackBaron94/Latin-Numerals-Translator-and-Quiz" > 
  <img src="https://codecov.io/gh/BlackBaron94/Latin-Numerals-Translator-and-Quiz/graph/badge.svg?token=QXBRFLQ1JI"/> 
  </a>


  <p align="center">
    Ένα project που μεταφράζει λατινικούς αριθμούς, δείχνει την αντιστοίχιση των αριθμών και τους κανόνες σύνταξης λατινικών αριθμών, 
    και έχει κουίζ μετάφρασης!
    </p>
</div>

## Περιεχόμενα
- [Περιγραφή Project](#περιγραφή-project)
- [Οδηγίες Εγκατάστασης](#οδηγίες-εγκατάστασης)
- [Λειτουργίες](#λειτουργίες)
- [Περιορισμοί](#περιορισμοί)
- [Χρήση](#χρήση)
- [Μελλοντικές Προσθήκες](#μελλοντικές-προσθήκες)
- [Επικοινωνία](#επικοινωνία)

## Περιγραφή Project 

Η εφαρμογή δημιουργήθηκε με σκοπό να μεταφράζει και να μαθαίνει στο χρήστη τους κανόνες των λατινικών αριθμών. Οι δυνατότητες
περιλαμβάνουν την μετάφραση αμφιδρόμως, δηλαδή από λατινικά σε αριθμούς δεκαδικού συστήματος και το αντίστροφο, προβολή 
κανόνων σύνταξης και αντιστοίχισης λατινικών αριθμών με αριθμούς δεκαδικού συστήματος, και κουίζ με μετάφραση από και 
προς λατινικούς αριθμούς! Επιπλέον, αν ο χρήστης απαντήσει πάνω από 4 φορές σωστά, βλέπει την καταμέτρηση των 
σωστών απαντήσεων!

### Τεχνολογίες και βιβλιοθήκες που χρησιμοποιήθηκαν

* [![Python][python.org]][Python-url]
* [![PyQt5][PyQt5.python]][PyQt5-url] PyQt5 
* [<img src="https://avatars.githubusercontent.com/u/1215332?v=4" alt="PyInstaller_Logo" width="40" />][PyInstaller-url] PyInstaller
* [<img src="https://static-00.iconduck.com/assets.00/githubactions-icon-2048x2048-ipqow27x.png" alt="GithubActions_Logo" width="40" />][GitHubActions-url] GithubActions (CI testing pipeline)

### CI/CD

Το project χρησιμοποιεί [GitHub Actions](https://github.com/features/actions) για την αυτοματοποιημένη εκτέλεση δοκιμών (tests) σε κάθε αλλαγή στον κώδικα (push ή pull request στο main branch).

Ορίζεται στο αρχείο `.github/workflows/tests.yml` και περιλαμβάνει αυτόματη εγκατάσταση dependencies και εκτέλεση των tests με `pytest`.

Το badge στο πάνω μέρος δείχνει την τρέχουσα κατάσταση των tests.

### Αρχεία του Project


- main.py: Περιέχει τη συνάρτηση main() που ξεκινάει το Application και εμφανίζει το παράθυρο
- gui.py: Το αρχείο αυτό περιέχει τον κώδικα για το GUI. Εδώ υλοποιούνται τα παράθυρα τα κουμπιά και οι λοιπές
διεπαφές με τον χρήστη, ώστε να μπορει να αλληλεπιδρά με την εφαρμογή.
- logic.py: Στον κώδικα του αρχείου αυτού περιλαμβάνονται όλες οι επιχειρησιακές λειτουργίες και η επεξεργασία
των δεδομένων. Εδώ υλοποιούνται οι βασικοί αλγόριθμοι και η λογική πίσω από τη μετάφραση των αριθμών.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Οδηγίες Εγκατάστασης


- Executable

Το onefile .exe είναι fully portable και δεν υπάρχουν προαπαιτούμενα. Κάνοντας clone το repo και τρέχοντας
το Latin-Numerals-Translator-and-Quiz.exe είστε έτοιμοι!

1. Clone του repo
   ```sh
   git clone https://github.com/BlackBaron94/Latin-Numerals-Translator-and-Quiz.git
   ```

- Κώδικας

Για να τρέξει το αρχείο .py χρειάζεται εγκατεστημένη έκδοση 3. Python καθώς και το πακέτο βιβλιοθήκης PyQt5

2. Έλεγχος εγκατεστημένης έκδοσης Python
   ```sh
   python --version
   ```
3. Έλεγχος εγκατάστασης pip
   ```sh
   pip -v
   ```

4. Εγκατάταση πακέτου PyQt5
   ```sh
   pip install PyQt5
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Λειτουργίες

1. **Numerals Translator**

Ανοίγει παράθυρο που επιτρέπει τη μετάφραση από και προς λατινικούς αριθμούς. Η αντιστροφή 
μετάφρασης πραγματοποιείται με click στο κουμπί με τα βελάκια. 
Στη μετάφραση από λατινικούς αριθμούς το πρόγραμμα αγνοεί τους χαρακτήρες που δεν είναι
λατινικοί αριθμοί, ενώ στη μετάφραση σε λατινικούς αριθμούς το πρόγραμμα δεν μεταφράζει
αν εντοπίσει χαρακτήρα κι όχι αριθμό.

---

2. **Numerals Rules**

Εμφανίζει παράθυρο με την αντιστοίχιση λατινικών αριθμών σε αριθμούς δεκαδικούς συστήματος καθώς
και κανόνες σύνταξης λατινικών αριθμών. Το παράθυρο μπορεί να μένει ανοιχτό ακόμα και μαζί με το
παράθυρο του Κουίζ ή του μεταφραστή, με σκοπό να βοηθάει χρήστες που θέλουν να μάθουν εμπράκτως!

---

3. **Quiz**

Εμφανίζει παράθυρο στο οποίο ο χρήστης μπορεί να απαντήσει σε ερώτηση Quiz μετάφρασσης.
Το πρόγραμμα εμφανίζει τυχαία επιλεγμένο αριθμό από το 1 ως το 3999. Όταν ο χρήστης κάνει λάθος
το πρόγραμμα δείχνει την σωστή απάντηση.
Ο αριθμός έχει 50% πιθανότητα να είναι στην κάθε μορφή. Αν ο χρήστης απαντήσει σε 5 ερωτήσεις
σωστά, βλέπει το σερί σωστών ερωτήσεων!

---

4. **Exit**

Τερματισμός του προγράμματος.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Περιορισμοί

Για την απεικόνιση των αριθμών 5.000, 10.000 και ούτω καθεξής, μέχρι κάποιο σημείο χρονικά 
χρησιμοποιούνταν επανειλημμένα ο χαρακτήρας M (1.000), ενώ αργότερα καθιερώθηκε να επαναλαμβάνονται 
τα σύμβολα V, X και λοιπά, με μία παύλα απο πάνω τους, δηλαδή V̅, X̅ και ούτω καθεξής. Επειδή η 
εισαγωγή αυτών των χαρακτήρων από τον χρήστη είναι προβλημματική, το πρόγραμμα δέχεται την επανάληψη
του χαρακτήρα M ως τρόπου μέτρησης αυτών των μεγάλων αριθμών, και δεν ζητά στο κουίζ μετάφραση 
αριθμών μεγαλύτερων του 3.999.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Χρήση

Υπάρχει διαθέσιμο video demo [εδώ](https://drive.google.com/file/d/1aruY7uyhJLd78Xq2Vgn0g6eC_az0DaOR/view?usp=drive_link).

Εναλλακτικά, παρακάτω φαίνονται παραδείγματα χρήσης με εικόνες.

---

> **Αυτό είναι το κύριο μενού της εφαρμογής.**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-Translator-and-Quiz/Latin-Numerals-Translator-and-Quiz-Main-Menu.jpg" alt="Latin-Numerals-Translator-and-Quiz-Main-Menu" width="500"/>
</div>

---

> **Παρακάτω φαίνεται το παράθυρο του μεταφραστή και η εμφάνιση του αποτελέσματος και στις δύο περιπτώσεις μετάφρασης**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-Translator-and-Quiz/Latin-Numerals-Translator-and-Quiz-Translator-Empty.jpg" alt="Latin-Numerals-Translator-and-Quiz-Translator-Empty" width="500" style="display: inline-block;"/>
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-Translator-and-Quiz/Latin-Numerals-Translator-and-Quiz-Translator-Latin-ToDec.jpg" alt="Latin-Numerals-Translator-and-Quiz-Translator-Latin-ToDec" width="500" style="display: inline-block;"/>
    
</div>

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-Translator-and-Quiz/Latin-Numerals-Translator-and-Quiz-Translator-Dec-To-Lat.jpg" alt="Latin-Numerals-Translator-and-Quiz-Translator-Dec-To-Lat" width="500"/>
</div>

---

> **Παρακάτω φαίνεται το παράθυρο Κουίζ ανοιχτό με τους κανόνες και το κύριο μενού καθώς και το μήνυμα σε περίπτωση συνεχόμενων σωστών απαντήσεων.**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-Translator-and-Quiz/Latin-Numerals-Translator-and-Quiz-Quiz-Empty.jpg" alt="Latin-Numerals-Translator-and-Quiz-Quiz-Empty" width="500" style="display: inline-block;"/>
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-Translator-and-Quiz/Latin-Numerals-Translator-and-Quiz-Quiz-Streak.jpg" alt="Latin-Numerals-Translator-and-Quiz-Quiz-Streak" width="500" style="display: inline-block;"/>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Μελλοντικές Προσθήκες

- [X] Προσθήκη Κουίζ.
- [ ] Προσθήκη επιλογής για ελληνική γλώσσα στο κύριο μενού.
- [ ] Διόρθωση εσφαλμένης διατύπωσης λατινικού αριθμού από τον χρήστη στον μεταφραστή.
- [ ] Δυνατότητα συγκροτημένου κουίζ με επιλογή αριθμού ερωτήσεων, 
τύπου ερωτήσεων, δυνατότητα skip ερώτησης, παρουσίαση αποτελεσμάτων
και σωστών απαντήσεων.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Επικοινωνία

Γιώργος Τσολακίδης - [Linked In: Giorgos Tsolakidis](https://www.linkedin.com/in/black-baron/) - black_baron94@hotmail.com 

Project Link: [Latin Numerals Translator and Quiz](https://github.com/BlackBaron94/Latin-Numerals-Translator-and-Quiz)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://python.org/
[PyQt5.python]: https://img.shields.io/badge/-PyQt-004400?style=flat&logo=Qt
[PyQt5-url]: https://pypi.org/project/PyQt5/
[PyInstaller-url]: https://pyinstaller.org/
[GithubActions.icon]: https://static-00.iconduck.com/assets.00/githubactions-icon-2048x2048-ipqow27x.png
[GithubActions-url]: https://github.com/features/actions
