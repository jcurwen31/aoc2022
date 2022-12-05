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

            def elve1Elems = []
            for (i in low1..high1) {
                elve1Elems << i
            }
            def set1 = elve1Elems.toSet()

            def elve2Elems = []
            for (i in low2..high2) {
                elve2Elems << i
            }
            def set2 = elve2Elems.toSet()

            if (set1.intersect(set2).size() > 0){
                println("OVERLAP")
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
