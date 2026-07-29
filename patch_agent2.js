const fs = require('fs');

let indexHtml = fs.readFileSync('index.html', 'utf8');
indexHtml = indexHtml.replace(/A4ec4ChLkqKsNqJDSDRSYKBXtNC3txgFpgJXEux5pump/g, 'coming soon on pons family');
indexHtml = indexHtml.replace(/Solana/g, 'Robinhood Chain');
indexHtml = indexHtml.replace(/solana/g, 'robinhoodchain');
indexHtml = indexHtml.replace(/Pump\.fun/g, 'Pons Family');
indexHtml = indexHtml.replace(/pump\.fun/g, 'ponsfamily.com');
fs.writeFileSync('index.html', indexHtml);

let signupHtml = fs.readFileSync('signup.html', 'utf8');
signupHtml = signupHtml.replace(/Solana/g, 'Robinhood Chain');
signupHtml = signupHtml.replace(/solana/g, 'robinhoodchain');
signupHtml = signupHtml.replace(/Pump\.fun/g, 'Pons Family');
signupHtml = signupHtml.replace(/pump\.fun/g, 'ponsfamily.com');
signupHtml = signupHtml.replace(/AUTH_PHANTOM/g, 'AUTH_METAMASK');
signupHtml = signupHtml.replace(
    /onclick="alert\([^)]+\)"/g,
    `onclick="if(window.ethereum){ window.ethereum.request({method: 'eth_requestAccounts'}).then(() => alert('Connected to Robinhood Chain!')).catch(e => console.error(e)) } else { alert('Please install MetaMask!') }"`
);
fs.writeFileSync('signup.html', signupHtml);

console.log('Replaced content in index.html and signup.html');
