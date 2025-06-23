const express = require('express');
const fs = require('fs');
const serverless = require('serverless-http');

const app = express();
const port = process.env.PORT || 3000;

// Service configuration
const config = {
    name: 'SUchedule',
    term: '202402',
    version: 58,
    dates: {
        start: '2025-02-03',
        end: '2025-06-04'
    }
};

// Testing endpoint
app.get('/', (req, res) => {
    res.json({
        name: config.name
    });
});

// Version endpoint
app.get('/version', (req, res) => {
    res.json({
        name: config.name,
        term: config.term,
        version: config.version,
        'start-date': config.dates.start,
        'end-date': config.dates.end
    });
});

// Data endpoint
app.get('/data', (req, res) => {
    try {
        const data = JSON.parse(fs.readFileSync('./data.json', 'utf8'));
        data.term = config.term;
        data.version = config.version;
        data.infoLink = `https://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=${data.term}&crn_in=`;
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Error reading data file' });
    }
});

// For local development
if (process.env.NODE_ENV !== 'production') {
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}

// For AWS Lambda
module.exports.handler = serverless(app); 