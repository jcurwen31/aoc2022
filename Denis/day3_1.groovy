File file = new File("puzzle_day3_1")
def line, noOfLines = 0;
def list = new ArrayList<Integer>()
def result = 0
def myScore = 0
def winScore = 0

file.withReader { reader ->
    while ((line = reader.readLine()) != null) {
        println("line = $line")
        def common = findCommonElem(line)
        def score = getScore(common)
        println("value $common = $score")
        result+=score
    }

}
println "Nbr lines ${noOfLines}"
println "result = ${ result }"

def findCommonElem(line) {
    def middle = line.size() / 2 as Integer
    def pack1 = line.substring(0, middle)
    def pack2 = line.substring(middle, line.size())
    def chars1 = new HashSet<>(pack1.toCharArray() as List<Character>)
    def chars2 = new HashSet<>(pack2.toCharArray() as List<Character>)
    def commonChar = chars2.intersect(chars1)
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
