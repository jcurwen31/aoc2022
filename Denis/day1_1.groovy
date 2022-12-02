File file = new File("puzzle_day1_1")
def line, noOfLines = 0;
def totalCal = 0
def bestTotalCal = 0
file.withReader { reader ->
    while ((line = reader.readLine()) != null) {
        def cal = line.size() == 0 ? "" : line as Integer
        if (cal != "") {
            totalCal += cal
        } else {
            if (totalCal > bestTotalCal) {
                bestTotalCal = totalCal
            }
            totalCal = 0
        }
        println "${line}"
        println "${cal}"
        noOfLines++
    }
}
println "Nbr lines ${noOfLines}"
println "bestTotalCal ${bestTotalCal}"