import React, {useState} from 'react';

const GraphButton = (props) => {
    const [isEmpty, setIsEmpty] = useState(true);
    const handleRedirect = () => {
        window.open(`https://oauth.vk.com/authorize?client_id=7819309&display=page&response_type=code&v=5.120&state=4194308`)
    };
    const postData = async (url, data) => {
        const res = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
        });
        return res.json();
    }
    const buildGraph = async() => {
        await postData('http://localhost:8000/', props.plotType === 'wall' ? 
                {owner_id: props.data.owner_id, offset: props.data.offset, count: props.data.count, filter: 'all', access_token: props.data.accessCode} : 
                {group_id: props.data.group_id, app_id: props.data.app_id, timestamp_from: props.data.from, timestamp_to: props.data.to, interval: props.data.interval, access_token: props.data.accessCode}
        ).then(data => props.setGraph(data))

    }
    const buttonOnClick = () => {
        props.data.accessCode === '' ? setIsEmpty(true) : setIsEmpty(false)
        isEmpty === true ? handleRedirect() : buildGraph()
    }
    return (
        <button onClick={buttonOnClick} className={props.styleProp}>
            Построить график
        </button>
    )
}

export default GraphButton;