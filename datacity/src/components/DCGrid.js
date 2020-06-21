import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';

class DCGrid extends React.Component {
    constructor(props) {
        super(props)
        this.state = {

        }
        this.isInit = false
        this.ignoreFields = []
    }

    processRows(data) {
        var res = {}
        let headers = Object.keys(data)
        for(let counter = 0; counter < headers.length; counter++) {
            let name = headers[counter]
            if(!(name in this.ignoreFields))
                res[name] = data[name]
        }
        return [res]
    }

    processData(data) {
        console.log(data)
        var headers = this.processColumnData(data)
        var rows = this.processRows(data)
        return {'headers': headers, 'rows': rows}
    }

    processColumnData(data) {
        var res = []
        var headers = Object.keys(data)
        for(let counter = 0; counter < headers.length; counter++) {
            let name = headers[counter]
            if(!(name in this.ignoreFields))
            res.push({headerName: name, field: name})
        }
        return res
    }

    render() {
        if(!this.isInit) {
            this.ignoreFields = this.props.ignoreFields
            var results = this.processData(this.props.data);
            var headers = results['headers']
            var rows = results['rows']
            this.setState(Object.assign({},  this.state, {'columnDefs':headers, 'rowData':rows}))
            this.isInit = true
            return ''
        }

        return (
            <div
                className="ag-theme-alpine"
                style={{
                    height: '250px',
                    width: 'auto',
                    maxWidth: '2000px'}}
            >
                <AgGridReact
                    columnDefs={this.state.columnDefs}
                    rowData={this.state.rowData}>
                </AgGridReact>
            </div>
        );
    }
}

export default DCGrid;