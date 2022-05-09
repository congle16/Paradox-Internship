# GIT & PYTHON BASIC

## 1. GIT

    ### LÀM VIỆC VỚI BRANCH
        1. Tổng quan
        Đối với các dự án lớn, mỗi thành viên tham gia sẽ nhận được nhiều task từ leader, vì vậy việc xử lý các task này cùng một thời gian là rất khó vì dễ bị đụng code. Để giải quyết vấn đề  này thì chúng ta sẽ sử dụng branch của Git, tương ứng với mỗi nhiệm vụ chúng ta sẽ tạo một branch và làm việc trên đó, các branch này sẽ hoạt động riêng lẻ và không ảnh hưởng lẫn nhau.
        -> Branch là những phân nhánh ghi lại luồng thay đổi của lịch sử, các hoạt động trên mỗi branch sẽ không ảnh hưởng lên các branch khác nên có thể tiến hành nhiều thay đổi cùng lúc trên một repository, giúp giải quyết được nhiều nhiệm vụ cùng lúc.
        
        2. Branch master
        Khi chúng ta tạo một repository thì Git sẽ thiết lập một branch master, nghĩa là nó sẽ tự tạo một branch master và mọi hoạt động của ta lúc này sẽ nằm trên branch master. Chúng ta có thể xem đây là branch mặc định đóng vai trò cập nhật dữ liệu và đồng bộ với remote repository.
        Giả sử ta đang có 10 tasks, lúc này ta không nên làm việc trực tiếp trên branch master mà hãy tạo ra những branch khác và branch master chỉ nên dùng để pull code từ remote branch master và merge với các branch còn lại. Mỗi branch làm việc sẽ được ghi lại lịch sử nên trong quá trình làm việc ta hòan toàn có thể rollback lại quá khứ vào chỉ mục index mà Git đã lưu.

        3. Syntax
        - Tạo mới branch
`$ git branch <branch_name>`

        - Chuyển đổi branch đang làm việc
`$ git checkout <branch_name>`

_Note: Trước khi checkout sang branch khác thì ta cần lưu lại tất cả những gì đã làm bằng lệnh commit. Nếu không commit thì sau khi chuyển sang branch khác những thay đổi sẽ không được lưu lại trong history và sau này ta không thể rollback lại được._

        4. Merge branch - Xử lý conflict
        Merge branch tức là ta gộp hai branch lại với nhau, thao tác này thường dùng để merge branch khác vào branch master trước khi push lên remote repository, hoặc merge hai branch thành một để giải quyết chung một task.
        Để merge branch bất kỳ vào với branch hiện tại, giả sử đang ở branch master, ta sử dụng cú phát sau: 
`$ git merge <branch_name>`

        Xử lý conflict: Giả sử ta đang làm hai task trên cả hai branch task1 và task2, cả hai đều cùng chỉnh sửa một file, lúc này merge task1 vào task2 sẽ bị xung đột (conflict), vì vậy ta sẽ cần phải sửa xung đột đó thì thao tác merge mới hoàn thành 100%.
        Đoạn bị xung đột được bắt đầu bằng <<<<<<< HEAD và kết thúc tại >>>>>>> branch1, được ngăn cách bởi đường =======. Trong đó đoạn trên là của branch hiện tại (branch2) và đoạn dưới là của branch cần merge (branch1).
        Nhiệm vụ bây giờ của ta là xem xét nội dung bị conflict đó cần sửa chỗ nào, sau đó xóa đi những kí tự trên. Cuối cùng commit để hoàn thành thao tác merge.

        5. Xóa local branch
        Thông thường mỗi một nhiệm vụ chúng ta sẽ làm việc trên một branch khác nhau, vì vậy sau khi hoàn thành một nhiệm vụ nào đó chúng ta sẽ thực hiện thao tác merge vào branch master, bước tiếp theo là thực hiện xóa branch đó để tránh xung đột và dễ quản lý mã nguồn hơn.
        * Khi tạo một branch và thực hiện một số commit trên đó nhưng chưa thực hiện thao tác merge vào branch master thì nó đang ở trạng thái not fully merged, còn nếu đã merge rồi thì sẽ ở trạng thái fully merged
        Để xóa local branch, ta thực hiện:
`$ git branch -d <branch_name>`

_Note: Không thể xóa branch mà ta đang làm việc, ví dụ nếu ta đang làm việc trên branch client thì ta không thể xóa branch client, thay vào đó ta phải checkout sang branch khác để xóa branch client. Ta cũng có thể xóa branch ở trạng thái fnot fully merged bằng câu lệnh:_

`$ git branch -D <branch_name>`

_Lúc này ta phải cân nhắc vì nếu xóa branch thì sẽ mất đi các commit đã thực hiện trước đó._

````
    ### TÌM HIỂU COMMIT
    1. Ba trạng thái
    Mỗi tập tin trong Git được quản lý dựa trên ba trạng thái là committed, modified, và staged. Trong đó: 
        - Committed có nghĩa là dữ liệu đã được lưu trữ một cách an toàn trong cơ sở dữ liệu, tức là những gì ta đã commit thành công.
        - Staged là ta đã đánh dấu sẽ commit phiên bản hiện tại của một tập tin đã chỉnh sửa trong lần commit sắp tới. Trạng thái này xảy ra khi ta sử dụng lệnh git add <file_name> nhưng chưa commit.
        - Modified có nghĩa là ta đã thay đổi tập tin nhưng chưa commit vào cơ sở dữ liệu, tức là ta chưa sử dụng lênh git add và git commit.

        Như vậy 3 trạng thái này đã tạo ra 3 phần riêng biệt của một dự án có sử dụng Git:
        - Khu vực Git (Git directory): Là thư mục lưu trữ siêu dữ liệu (metadata) và cơ sở dữ liệu của dự án, thư mục này sẽ bị ẩn bởi hệ điều hành Windows nên ta phải bật chức năng hiển thị file ẩn thì mới thấy được.  Khu vực này sẽ tiếp nhận và lưu trữ các commit từ stage area.
        - Khu vực làm việc (Working directory):  Nếu ta không sử dụng Remote repository thì đây là bản sao của dự án, còn không thì đây là thư muc chính của dự án và branch master chính là bản chính, còn các branch mới tạo là branch bản sao.
        - Khu vực tổ chức (staging area): đây là một tập tin đơn giản nằm trong thư mục git, nó sẽ chứa thông tin về trạng thái của một file trong dự án.
        Như vậy nếu ta thay đổi một file nhưng chưa sử dụng lệnh git add và git commit thì file đó ở trạng thái modified, còn nếu đã sử dụng lệnh git add thì sẽ ở trạng thái staged, còn đã commit thì sẽ ở trạng thái committed.

````
![image](https://git-scm.com/book/en/v2/images/areas.png)
````

        Từ hình trên, khi làm việc với Git bạn theo tiến trình như sau:

        -> Bạn code, sửa đổi các file trong 1 Thư mục làm việc (Working tree)
        -> Bạn tổ chức những sự thay đổi nào muốn commit tiếp theo, cơ bản là việc đánh dấu sự thay đổi vào khu vực 2 Khu vực sắp xếp (staging)
        -> Bạn thực hiện commit để các file đánh dấu trong staged lưu vào 3 Git (database) như nhưng snapshot (chụp file)

    2. Mô hình kho chứa dữ liệu
    
    + Git Objects
        Khi chúng ta chạy lệnh $ git init thì một thư mục ẩn được tạo ra đó là .git, thư mục này sẽ chứa toàn bộ database và các thao tác của dự án, nó có một số thư mục con và một số file quan trọng gồm: HEAD, branches/, config, description, hooks/ index, info/, objects/, refs/.
        Trong đó bạn cần chú ý đến thư mục objects vì đây là thư mục chứa toàn bộ database, nó có 4 objects như sau:
            ~ tree: là directory
            ~ blob: là file
            ~ commit
            ~ tag
    + Mô hình đối tượng 1 branch
        Khi ta thực hiện một commit, Git sẽ tạo một đối tượng commit và có chứa các con trỏ trỏ tới ảnh của nội dung mà ta đã tổ chức tại stage, ngoài ra còn chứa thông tin tác giả, thông điệp, cũng có thể chứa các con trỏ khác trỏ tới các commit cha của commit đó. Commit đầu tiên sẽ không có cha, commit thứ ha trở đi sẽ có một cha hoặc nhiều cha nếu nó được merge từ nhiều branch.
        Giả sử có 3 tập tin và ta sẽ tổ chức cả 3 tập tin vào stage để commit. Lệnh commit sẽ băm cả 3 file và lưu chúng dưới dạng đối tượng tree (thư mục), trong tree sẽ chứa tất cả các blod (tức là 3 file trên) và mỗi blod sẽ trỏ đến file gốc của nó. Sau đó nó tạo một đối tượng commit chứa các thông tin metadata như author, email, message ... và đặc biệt đối tượng commit này có 1 con trỏ trỏ tới đối tượng tree, vì vậy có thể tái tạo lại history thông qua đối tượng commit này.
        Như vậy đối tượng tree và blod ta gọi là snapsot.
        Nếu ta thay đổi dữ liệu cho một trong ba file và tiếp tục thực hiện một lệnh commit thì lúc này ngoài các thông tin như trên, đối tượng commit còn tạo thêm một con trỏ và trỏ tới đối tượng commit trước đó.
    + Mô hình đối tượng nhiều branch
        Khi ta tạo một nhánh (branch) thực chất là bạn đang tạo một con trỏ và trỏ tới commit mới nhất tại thời điểm thực thi lệnh. Chúng ta có tên nhánh mặc định là Master Branch
    + Con trỏ HEAD
        Git có một con trỏ đặc biệt tên là HEAD, đây là con trỏ sẽ trỏ tới một branch nội bộ trong repository của bạn.

    3. Amend, thay đổi commit cuối cùng
        Trong một số trường hợp ta commit nhưng bị quên add một số file nào đó và bạn không muốn tạo ra một commit mới thì có thể sử dụng lệnh commit kết hợp tham số --amend để gộp các file đó và bổ sung vào commit cuối cùng, vì vậy không tạo ra commit mới.  
        Nếu ta thực hiện lệnh này ngay sau commit cuối cùng mà không thay đổi gì thêm thì ảnh của commit cuối cùng đó không thay đổi gì, chỉ là nội dung message thay đổi mà thôi. Trình soạn thảo sẽ hiển thị để ta thay đổi message, đương nhiên ta có thể để message mặc định mà git đã tạo ra, và message này sẽ ghi đè lên message trước đó.
        * Loại bỏ tập tin đã đưa vào stage
        Khi ta đã thêm một file nào đó vào stage (trạng thái staged, đây là trạng thái sẽ được đưa vào blod khi committed) nhưng sau đó muốn loại bỏ nó ra khỏi stage thì có thể sử dụng lệnh reset HEAD.
    
    4. Stash trở về trạng thái ban đầu
        Git stash được sử dụng khi muốn lưu lại các thay đổi chưa commit, thường rất hữu dụng khi ta muốn đổi sang 1 branch khác mà lại đang làm dở ở branch hiện tại.

    5. Phân nhánh với Rebase
        + Lệnh git merge sử dụng để gộp nhánh, gộp nhánh này vào nhánh khác. Khi gộp nhánh git thường căn cứ vào 3 commit, để tạo ra một commit gộp, nếu có xung đột cần xử lý.
        Giả sử có hai nhánh master và beta như sau:

````
![image](https://raw.githubusercontent.com/xuanthulabnet/learn-git/master/docs/git010.png)
````

        Để gộp các commit trong nhánh beta vào nhánh master thì chuyển làm việc trên master và thực hiện lệnh:
````
`$ git merge beta`
````
        Sơ đồ và kết quả của lệnh git merge như hình sau:

````
![image](https://raw.githubusercontent.com/xuanthulabnet/learn-git/master/docs/git011.png)
````

        + Lệnh git rebase cũng gộp các commit từ nhánh này vào nhánh khác, bằng cách xây dựng lại các commit base kế thừa từ nhánh khác và viết lại lịch sử commit sau các commit cơ sở mới.
        Ví dụ, để gộp nhánh beta vào master, đứng ở master thực hiện lệnh
````
`$ git rebase beta`
````
````
![image](https://raw.githubusercontent.com/xuanthulabnet/learn-git/master/docs/git012.png)
````

        Như trên hình trên, trước thời điểm rebase, nhánh master có các commit cơ sở giống với nhánh beta đó là: C1, C2, C2

        Lệnh git rebase sẽ đưa toàn bộ nhánh beta làm base của master, do vậy các commit tiếp theo sau commit cơ sở ban đầu của master sẽ được nối tiếp vào, trong đó có thay đổi lại lịch sử commit, cũng sử lý xung đột giữa commit B2 và D1 để viết lại commit D1 thành D1'

        Tương tự, nếu gộp master vào beta thì sơ đồ có thể là:
````
![image](https://raw.githubusercontent.com/xuanthulabnet/learn-git/master/docs/git013.png)
````

````

    ### LÀM VIỆC VỚI REMOTE
    (Thực hành)

***

## PYTHON BASIC

    * KHAI BÁO BIẾN

    * HÀM PRINT

    * STRING

    * NUMBER

    * LIST

    * ARRAY

    * SET

    * TUPLE

    * DICTIONARY

    * OPERATORS

    * FOR - WHILE

    * RANGE

    * IF - ELIF - ELSE

    * SWITCH - CASE

    * FUNCTION

    * CLASS

    * LAMBDA

    * MODULE
