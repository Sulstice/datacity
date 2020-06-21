import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';
import './ag.css'


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
            if((this.ignoreFields.includes(name))) {
                continue
            }
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
            if((this.ignoreFields.includes(name))) {
                continue
            }
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

        var width = window.screen.width-150;



        return (
            <div
                style={{ height: '250px', width: '100%' }} className="ag-theme-alpine"

            >
                <AgGridReact
                    onGridReady={ params => {
                        this.gridApi = params.api;
                        params.columnApi.sizeColumnsToFit(width) }
                    }
                    columnDefs={this.state.columnDefs}
                    rowData={this.state.rowData}>
                </AgGridReact>
            </div>
        );
    }
}

export default DCGrid;