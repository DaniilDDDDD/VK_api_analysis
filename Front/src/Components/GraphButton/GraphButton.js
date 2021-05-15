import React from 'react';

const GraphButton = (props) => {

    const postData = async (url, data) => {
        const res = await fetch(url, {
            headers: {
              'Content-Type': 'application/json'
            },
            method: 'POST',
            body: JSON.stringify(data),
        });
        return res.json();
    }
    const buildGraph = async() => {
        props.plotType !== 'tags' ? await postData(`http://localhost:8000/${props.sourceType}/${props.plotType}/`, props.sourceType === 'wall' ?
                {owner_id: [String(props.data.owner)], offset: [String(props.data.offset)], count: [String(props.data.count)], filter: ['all'], access_token: [String(props.data.accessCode)]} :
                {group_id: [String(props.data.group)], app_id: [String(props.data.app)], timestamp_from: [String(props.data.from)], timestamp_to: [String(props.data.to)], interval: [String(props.data.interval)],intervals_count: [String(props.data.intervalsCount)], access_token: [props.data.accessCode]}
        ).then(data => props.setGraph(data.image))
        : await postData(`http://localhost:8000/tag/`, {owner_id: [String(props.data.owner)], offset: [String(props.data.offset)], count: [String(props.data.count)], filter: ['all'], access_token: [String(props.data.accessCode)]})
        .then(data => props.setGraph(data))
    }
    const buttonOnClick = () => {
        buildGraph()
    }
    return (
        <button onClick={buttonOnClick} className={props.styleProp}>
            Build Graph
        </button>
    )
}

export default GraphButton;