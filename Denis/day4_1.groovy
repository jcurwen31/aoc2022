File file = new File("puzzle_day4_1")
def line, noOfLines = 0;
def list = new ArrayList<Integer>()
def result = 0
def myScore = 0
def winScore = 0

file.withReader { reader ->
    while ((line = reader.readLine()) != null) {
        println("line = $line")
        if (line) {
            def assigns = line.split(',')
            def elve1 = assigns[0].split('-')
            def elve2 = assigns[1].split('-')
            def low1 = elve1[0] as Integer
            def high1 = elve1[1] as Integer
            def low2 = elve2[0] as Integer
            def high2 = elve2[1] as Integer

            if (low1 <= low2 && high1 >= high2){
                println("1 INLUDES 2")
                result++
            } else  if (low2 <= low1 && high2 >= high1){
                println("2 INLUDES 1")
                result++
            } else {
                println("NO OVERLAP")
            }
        }


        noOfLines++
    }

}
println "Nbr lines ${noOfLines}"
println "result = ${ result }"
