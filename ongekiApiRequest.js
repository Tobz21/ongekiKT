(async () => {
    const { pbs, songs, charts } = await fetch(`https://kamai.tachi.ac/api/v1/users/me/games/ongeki/Single/pbs/all`)
        .then((r) => r.json())
        .then((r) => r.body);
    
    const songsByID = new Map(songs.map((s) => [s.id, s]));
    const chartsByID = new Map(charts.map((c) => [c.chartID, c]));
  
    const ratingCalculatorEntries = pbs.map((s) => {
      const song = songsByID.get(s.songID);
      const chart = chartsByID.get(s.chartID);
      const sheetDifficulty = chart.difficulty.toLowerCase();
      const sheetId = `${song.title}__onrt__${sheetDifficulty}`;
      return { sheetId, achievementRate: s.scoreData};
    });
    
    const blob = new Blob([JSON.stringify(ratingCalculatorEntries)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `ongekirating.tachi_${new Date().toISOString()}.json`;
    a.click();
    a.remove();
})();