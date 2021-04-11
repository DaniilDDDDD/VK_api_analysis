import './Graph.css'
import React, {useState} from 'react';
import GraphButton from '../GraphButton/GraphButton';
const Graph = () => {
    const [plotType,setPlotType] = useState('wall');
    const [owner,setOwner] = useState(0);
    const [offset,setOffset] = useState(0);
    const [count,setCount] = useState(0);
    const [group,setGroup] = useState(0);
    const [app,setApp] = useState(0);
    const [from, setFrom] = useState(0);
    const [to, setTo] = useState(0);
    const [interval, setInterval] = useState(0);
    const [accessCode, setAccessCode] = useState('');
    const [graph, setGraph] = useState('');
    const ownerOnChange = (e) => {
        setOwner(Number(e.target.value))
    }
    const offsetOnChange = (e) => {
        setOffset(Number(e.target.value))
    }
    const countOnChange = (e) => {
        setCount(Number(e.target.value))
    }
    const groupOnChange = (e) => {
        setGroup(Number(e.target.value))
    }
    const appOnChange = (e) => {
        setApp(Number(e.target.value))
    }
    const fromOnChange = (e) => {
        setFrom(Number(e.target.value))
    }
    const toOnChange = (e) => {
        setTo(Number(e.target.value))
    }
    const intervalOnChange = (e) => {
        setInterval(Number(e.target.value))
    }
    const accessCodeOnChange = (e) =>{
        setAccessCode(e.target.value)
    }
    const selectOnChange = (e) => {
        setPlotType(e.target.value);
    }
    const constructData = () => {
        return plotType === 'wall' ? {owner, offset, count, accessCode} : {group, app, from, to, interval, accessCode};
    }
    const data = constructData()
    return (
        <div >
            <div className=" mt-32">
                <div className="h-12 w-120 mx-auto bg-blue-200 rounded-t-lg">
                    <select onChange={selectOnChange} id="plot" className="float-right w-28 mt-3 mr-2 border-2 rounded-md outline-none border-blue-300 bg-blue-100">
                        <option selected="selected" value="wall">
                            Wall
                        </option>
                        <option value="stats">
                            Stats
                        </option>
                    </select>
                </div>
                <div className="h-96 w-120 mx-auto border-8 border-blue-200 overflow-hidden">
                    {graph !== '' ? <img className="h-96 w-120" src={graph} alt="graph"/> : null}
                </div>
                <div className="mx-auto h-36 w-120 border-2 border-t-0 bg-blue-200 border-blue-200">
                    {plotType === 'wall' ? <div>
                                            <div>
                                                <input onChange={ownerOnChange} id="owner_id" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Owner_id"/>
                                                <input onChange={offsetOnChange} id="offset" className="h-8 w-48 ml-4  outline-none pl-2 rounded-md text-lg" placeholder="Offset"/>
                                            </div>
                                            <div>
                                                <input onChange={countOnChange} id="count" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Count"/>
                                                <input onChange={accessCodeOnChange} id="accessCode" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Access_code"/>
                                            </div>
                                            <div>
                                                <GraphButton setGraph={setGraph} data={data} plotType={plotType} styleProp="h-10 w-40 float-right mr-2 mt-2 bg-blue-300 rounded-xl"/>
                                            </div>
                                           </div> : 
                                           <div>
                                            <div>
                                                <input onChange={groupOnChange} id="group_id" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Group_id"/>
                                                <input onChange={appOnChange} id="app_id" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="App_id"/>
                                            </div>
                                            <div>
                                                <input onChange={fromOnChange} id="from" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Timestamp_from"/>
                                                <input onChange={toOnChange} id="to" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Timestamp_to"/>
                                            </div>
                                            <div>
                                                <input onChange={intervalOnChange} id="interval" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Interval"/>
                                                <input onChange={accessCodeOnChange} id="accessCode" className="h-8 w-48 ml-4 mt-2 outline-none pl-2 rounded-md text-lg" placeholder="Access_code"/>
                                                <GraphButton setGraph={setGraph} data={data} plotType={plotType} styleProp="h-10 w-40 float-right mr-2 mt-2 bg-blue-300 rounded-xl" />
                                            </div>
                                          </div>}
                    
                </div>
            </div>
        </div>
    )
}

export default Graph