class ApiService{
    getData = (url) => {

        var request = new XMLHttpRequest()
        request.overrideMimeType("application/json")
        request.open('GET', url, false)
        request.send(null)
        return JSON.parse(request.responseText)
    }
}
export default ApiService;