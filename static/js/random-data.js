// 后端进行数据下载
/**
 *
 * @param data
 */
function download_file(data) {
    if (!data) {
        return
    }
    // console.log(data)
    let url = window.URL.createObjectURL(data.data)
    let link = document.createElement('a')
    link.style.display = 'none'
    link.href = url
    let filename = 'file.csv'
    if (data.headers['content-disposition'] !== '') {
        let contents = data.headers['content-disposition'].split('filename=')
        filename = contents[contents.length - 1]
    }
    link.setAttribute('download', filename)
    document.body.appendChild(link)
    link.click()
}

/**
 *
 * @param title
 * @param x_name
 * @param y_name
 * @returns {{yAxis: {data: *}, xAxis: {data: *}, legend: {data: []}, series: [], tooltip: {}, title: {text: *}}}
 */
function gen_option(title, x_name, y_name) {
    return {
        title: {
            text: title
        },
        tooltip: {},
        legend: {
            data: []
        },
        xAxis: {
            data: x_name
        },
        yAxis: {
            data: y_name
        },
        series: []
    }
}

/**
 *
 * @param orgindata
 * @returns {[][]}
 */
function transform_data(orgindata) {
    var tabeldata = []
    var columnames = []
    //获取各个属性名称，也就是各科目名称
    for (k in orgindata) {
        columnames.push(k)
    }
    // 获取单个属性所对应数据的长度
    var size = orgindata[columnames[0]].length
    // 对数据进行加工 将每行数据存放到一个数据结构中
    for (var i = 0; i < size; i++) {
        temp = new Map()
        for (k in orgindata) {
            temp[k] = orgindata[k][i]
        }
        tabeldata.push(temp)
    }
    return [columnames, tabeldata]
}

function filter_data(data, types) {
    var map_data = {}
    for (index in data) {
        if (is_in_datas(index, types)) {
            continue
        } else {
            map_data[index] = data[index]
        }
    }
    return map_data
}

/**
 *
 * @param data
 * @param datas
 * @returns {boolean}
 */
function is_in_datas(data, datas) {
    var flag = false
    let len = datas.length
    let i = 0
    for (i = 0; i < len; i++) {
        if (datas[i] === data) {
            flag = true
            break
        }
    }
    return flag
}

/**
 *
 * @param option
 * @param map_data
 * @param type_name
 * @returns {*}
 */
function fill_echart_data(option, map_data, type_name) {
    for (index in map_data) {
        option.legend.data.push({
            name: index
        })
        option.series.push({
            name: index,
            type: type_name,
            data: map_data[index]
        })
    }
    return option;
}

function test() {
    return {
        template: '<h>hello component!</h>',
        data: {},
        methods: {}
    }
}