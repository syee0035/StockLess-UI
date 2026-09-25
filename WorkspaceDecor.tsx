/* Decorative background for the workspace shell.
   Same language as the homepage — waves, leaves and dot grids in SVG, colours
   sampled from the StockLess background mockup. This is an app rather than a
   marketing page, so it is deliberately quieter: the artwork is pinned to the
   viewport edges, the centre column is left clear, and nothing here takes a
   pointer event or is read by a screen reader. */

function Leaf({ x, y, s, rot, fill, op }: {
  x: number; y: number; s: number; rot: number; fill: string; op: number;
}) {
  return (
    <g transform={`translate(${x} ${y}) rotate(${rot}) scale(${s})`} opacity={op}>
      <path d="M36 2C16 16 4 34 4 52c0 17 14 30 32 30s32-13 32-30C68 34 56 16 36 2Z" fill={fill} />
      <path d="M36 78V12" stroke="#FFFFFF" strokeOpacity=".5" strokeWidth="2.5" strokeLinecap="round" />
      <path d="M36 34 18 46M36 34l18 12M36 54 20 66M36 54l16 12"
        stroke="#FFFFFF" strokeOpacity=".3" strokeWidth="2" strokeLinecap="round" />
    </g>
  );
}

function Dots({ x, y }: { x: number; y: number }) {
  const circles = [];
  for (let i = 0; i < 4; i++) for (let j = 0; j < 3; j++)
    circles.push(<circle key={`${i}-${j}`} cx={i * 16} cy={j * 16} r="2.5" />);
  return <g transform={`translate(${x} ${y})`} fill="#9CC9A0" opacity=".45">{circles}</g>;
}

export function WorkspaceDecor() {
  return (
    <div className="ws-decor" aria-hidden="true">
      <svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">
        {/* a soft wash along the top edge and waves along the foot */}
        <path d="M0 0h1440v70c-300 104-500-32-820 32C360 138 206 60 0 168Z" fill="#EDF7E9" opacity=".7" />
        <path d="M0 900V742c236-62 470 54 752 8 282-46 488 56 688 12v138Z" fill="#DCEFD8" opacity=".75" />
        <path d="M0 900V812c282-46 526 50 846 10 264-32 432 42 594 10v68Z" fill="#B8DFBE" opacity=".55" />
        {/* leaves sit in the margins, outside the centred content column */}
        <Leaf x={40} y={120} s={0.5} rot={-18} fill="#8FBC8B" op={0.55} />
        <Leaf x={118} y={228} s={0.32} rot={34} fill="#A5CDA0" op={0.5} />
        <Leaf x={1310} y={150} s={0.44} rot={156} fill="#A6CEA4" op={0.55} />
        <Leaf x={1382} y={286} s={0.3} rot={200} fill="#9AC698" op={0.5} />
        <Leaf x={62} y={618} s={0.42} rot={14} fill="#8FBC8B" op={0.5} />
        <Leaf x={1338} y={648} s={0.36} rot={-26} fill="#A5CDA0" op={0.5} />
        <Dots x={1348} y={430} />
        <Dots x={56} y={402} />
      </svg>
    </div>
  );
}
