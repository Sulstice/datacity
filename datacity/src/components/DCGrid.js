import React from 'react';
import './App.css';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';

class DCGrid extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
        this.isInit = false;
    }

    processColumnData

    render() {
        if(!this.isInit) {
            this.setState(Object.assign({},  this.state, {'columnDefs':this.props.columnDefs, 'rowData':this.props.rowData}))
            this.isInit = true;
            return '';
        }
        return (
            <div
                className="ag-theme-alpine"
                style={{
                    height: '250px',
                    width: '600px' }}
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