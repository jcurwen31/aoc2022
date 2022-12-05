File file = new File("puzzle_day3_1")
def line, noOfLines = 0;
def list = new ArrayList<Integer>()
def result = 0
def myScore = 0
def winScore = 0

def stacks = []
file.withReader { reader ->
    while ((line = reader.readLine()) != null) {
        println("line = $line")
        stacks << line
        if (noOfLines % 3 == 2) {
            def common = findCommonElem(stacks)
            def score = getScore(common)
            println("value $common = $score")
            result+=score
            stacks = []
        }

        noOfLines++

    }

}
println "Nbr lines ${noOfLines}"
println "result = ${ result }"

def findCommonElem(stacks) {
    println("findCommonElem stacks = $stacks")
    def chars1 = new HashSet<>(stacks[0].toCharArray() as List<Character>)
    def chars2 = new HashSet<>(stacks[1].toCharArray() as List<Character>)
    def chars3 = new HashSet<>(stacks[2].toCharArray() as List<Character>)
    def commonChar = chars3.intersect(chars2.intersect(chars1))
    return commonChar[0]
}

def getScore(common) {
    def value = common as Integer
    if (value - 96 < 0 ) {
//        majuscule
        return value - 64 + 26
    }
    return value - 96
}
