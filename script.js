async function fetchLinks() {
    const queryParams = new URLSearchParams(window.location.search);
    const indexes = queryParams.get('q').split(',').map(Number);

    try {
        const response = await fetch('https://raw.githubusercontent.com/tyroruyk/bdix/main/src/bdix/bdixServers.txt');
        const text = await response.text();
        const lines = text.split('\n');

        // Filter lines based on indexes
        const filteredLines = lines.filter((_, index) => indexes.includes(index));

        // Display links
        document.getElementById('linksContainer').innerHTML = filteredLines.map(line => `<a href="${line}" target="_blank">${line}</a>`).join('<br>');
    } catch (error) {
        console.error('Error fetching links:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchLinks();
});
