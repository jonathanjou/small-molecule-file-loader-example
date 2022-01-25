from molecule_screener import screen_molecule

def test_everything_in_one_go():
    st = structure.load('test_target.maegz')
    r_st = structure.load('reference_complex.maegz')
    g = gridgen.load('test_grid.grd')
    tpo = {
        'energy': True,
        'num_poses': 672,
    }
    rt = -1

    s, sc, ds = screen_molecule('test_mae.mae', st, g, tpo, rt)
    assert s
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_mae.mae.gz', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_mae.maegz', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_csv.csv', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_csv.csv.gz', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_csv.csvgz', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_mae.mae', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_mae.mae.gz', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
    s, sc, ds = screen_molecule('test_mae.maegz', st, g, tpo, rt)
    assert score == 8.13418631
    assert structure.are_identical(ds, r_st)
